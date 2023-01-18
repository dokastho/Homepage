"""Site model (database) API."""
from datetime import datetime
import hashlib
import sqlite3
import uuid
import pathlib
import homepage
import flask


def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.

    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_db():
    """Open a new database connection.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    if 'sqlite_db' not in flask.g:
        db_filename = homepage.app.config['DATABASE_FILENAME']
        flask.g.sqlite_db = sqlite3.connect(str(db_filename))
        flask.g.sqlite_db.row_factory = dict_factory
        # Foreign keys have to be enabled per-connection.  This is an sqlite3
        # backwards compatibility thing.
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")
    return flask.g.sqlite_db


@homepage.app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    assert error or not error  # Needed to avoid superfluous style error
    sqlite_db = flask.g.pop('sqlite_db', None)
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
    target = flask.request.args.get('target')
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
    if 'logname' not in flask.session:
        return False
    username = flask.session['logname']
    connection = get_db()
    cur = connection.execute(
        "SELECT username "
        "FROM users "
        "WHERE username == ?",
        (username, )
    )

    # user must exist
    user = cur.fetchall()
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
    connection = get_db()
    cur = connection.execute(
        "SELECT password "
        "FROM users "
        "WHERE username == ? ",
        (username,)
    )

    # password must exist
    pw_hash = cur.fetchall()
    if len(pw_hash) == 0:
        return False

    # get db entry salt if present and encrypt password
    pw_hash = pw_hash[0]
    salt = pw_hash['password'].split("$")
    if len(salt) > 1:
        salt = salt[1]
        pw_str = encrypt(salt, password)
    else:
        pw_str = password

    # find an entry with encrypted password
    cur = connection.execute(
        "SELECT username "
        "FROM users "
        "WHERE username == ? AND password == ?",
        (username, pw_str,)
    )

    # user must exist
    user = cur.fetchall()
    if len(user) == 0:
        return False

    return username


def show_username() -> dict:
    """Handle the rendering of the username/sign in link."""
    logname = homepage.model.get_logname()
    context = {}
    if not logname:
        context["logname"] = "Sign In"
        context["logname_link"] = "/accounts/login/"
    else:
        context["logname"] = logname
        context["logname_link"] = f"/accounts/{logname}/"
    return context


def encrypt(salt, password):
    """One way decryption given the plaintext pw and salt from user db."""
    algorithm = 'sha512'

    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string


def delete_helper(resumeid, entryid, freq):
    """Delete an entry or update if freq > 1."""
    database = get_db()
    freq -= 1
    if freq == 0:
        # delete the entry
        cur = database.execute(
            "DELETE FROM entries "
            "WHERE entryid == ?",
            (entryid,)
        )
        cur.fetchone()

        # delete teids associated with this entry
        cur = database.execute(
            "DELETE FROM entry_to_tag "
            "WHERE entryid == ?",
            (entryid,)
        )
        cur.fetchone()

    else:
        if resumeid == 0:
            flask.abort(501)
        # update the entry
        cur = database.execute(
            "UPDATE entries "
            "SET frequency = ?, priority = ? "
            "WHERE entryid == ?",
            (freq, freq, entryid,)
        )
        cur.fetchone()

        # delete the entry in table resume_to_entry
        cur = database.execute(
            "DELETE FROM resume_to_entry "
            "WHERE entryid == ? "
            "AND resumeid == ?",
            (entryid, resumeid, )
        )
        cur.fetchone()

    # delete tags
    cur = database.execute(
        "DELETE FROM entry_to_tag "
        "WHERE resumeid == ? "
        "AND entryid == ?",
        (resumeid, entryid, )
    )
    cur.fetchall()


def rest_api_auth_user():
    """Standard user auth in rest api, returns logname and database connection."""
    logname = get_logname()
    if not logname:
        flask.abort(403)

    database = get_db()
    return logname, database


def print_log(msg: str, code: None) -> str:
    now = datetime.utcnow()
    now = now.strftime("%d/%b/%Y %H:%M:%S")
    print(f'localhost - - [{now}] {msg} {code} -')
