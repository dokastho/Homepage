"""Site model (database) API."""
from datetime import datetime
import hashlib
import uuid
import pathlib
import homepage
import flask
from utils import get_client


def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.

    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


@homepage.app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    assert error or not error  # Needed to avoid superfluous style error
    sqlite_db = flask.g.pop("sqlite_db", None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()


def get_uuid(filename):
    """Get image uuid."""
    stem = uuid.uuid4().hex
    suffix = pathlib.Path(filename).suffix
    uuid_basename = f"{stem}{suffix}"

    return uuid_basename


def get_target():
    """Return request target or /."""
    target = flask.request.args.get("target")
    if target is None or target == "":
        return "/"
    return target


def get_logname() -> str:
    """Get the logname either from session or http basic auth."""
    session_logname = check_session()
    basic_logname = check_authorization()
    if session_logname:
        return session_logname
    if basic_logname:
        return basic_logname

    return None


def check_session():
    """Check if logname exists in session."""
    if "logname" not in flask.session:
        return False
    username = flask.session["logname"]

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT username FROM users WHERE username == ?",
        "args": [username],
    }
    req_hdrs = {"content_type": "application/json"}
    user = get_client().get(req_data, req_hdrs)

    # user must exist
    if len(user) == 0:
        flask.session.clear()
        return False

    return username


def check_authorization(username=None, password=None):
    """Check if authorization in request matches credentials for a user."""
    if username is None or password is None:
        # auth must exist if username and password aren't provided
        if flask.request.headers.get("authorization") is None:
            return False

        # auth must have username and password in headers
        username = flask.request.authorization.get("username")
        password = flask.request.authorization.get("password")
        if username is None or password is None:
            return False

    # verify username and password match an existing user
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT password FROM users WHERE username == ?",
        "args": [username],
    }
    req_hdrs = {"content_type": "application/json"}
    pw_hash = get_client().get(req_data, req_hdrs)

    # password must exist
    if len(pw_hash) == 0:
        return False

    # get db entry salt if present and encrypt password
    pw_hash = pw_hash[0]
    salt = pw_hash["password"].split("$")
    if len(salt) > 1:
        salt = salt[1]
        pw_str = encrypt(salt, password)
    else:
        pw_str = password

    # find an entry with encrypted password
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT username FROM users WHERE username == ? AND password == ?",
        "args": [username, pw_str],
    }
    req_hdrs = {"content_type": "application/json"}

    # user must exist
    user = get_client().get(req_data, req_hdrs)
    if len(user) == 0:
        return False

    return username


def encrypt(salt, password):
    """One way decryption given the plaintext pw and salt from user db."""
    algorithm = "sha512"

    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode("utf-8"))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string
