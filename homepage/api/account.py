"""accounts interface."""
import uuid
import hashlib
import os
import homepage
import arrow
from homepage.common import model
from homepage.common.utils import get_client
from flask import abort, redirect, render_template, request, session


@homepage.app.route('/accounts/', methods=['POST'])
def accounts():
    """/accounts/?target=URL Immediate redirect. No screenshot."""
    with homepage.app.app_context():
        # check if target is unspecified or blank
        target = model.get_target()
        # get operation
        operation = request.form.get('operation')

        # create a login cookie
        if operation == "login":

            # get username and password from form
            uname = request.form['username']
            pword = request.form['password']

            # set session cookie
            if not do_login(uname, pword):
                return redirect("/accounts/login/?badlogin=1")
            session['logname'] = uname

        # create an account
        elif operation == "create":
            info = {
                "username": request.form.get("username"),
                "email": request.form.get("email"),
                "password": request.form.get("password")
            }
            if not do_create(info):
                # username is taken
                return redirect("/accounts/create/?baduser=1")

            session['logname'] = info['username']

        elif operation == "delete":
            do_delete()

        elif operation == "update_password":
            # user must be logged in
            if 'logname' not in session:
                abort(403)

            info = {
                "username": session['logname'],
                "old": request.form.get('old_password'),
                "new": request.form.get("password"),
                "verify_new": request.form.get("check_password"),
            }
            do_update_password(info)

        else:
            abort(400)  # invalid request

    return redirect(target)


def do_login(uname, pword):
    """Login user with username and password."""
    logname = model.check_authorization(uname, pword)
    if not logname:
        return False

    return True


def do_create(info):
    """Create account with info."""
    for i in info:
        if i == "":
            abort(400)

    utc = arrow.utcnow()
    local = utc.to('US/Pacific')
    timestamp = local.format()

    pp_str = model.get_uuid(info['file'].filename)
    pw_str = create_hashed_password(info['password'])
    
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT username FROM users WHERE username == ? ",
        "args": [info['username']],
    }
    req_hdrs = {
        'content_type': 'application/json'
    }
    user = get_client().get(req_data, req_hdrs)

    if len(user) != 0:
        return False

    # save image
    path = homepage.app.config["UPLOAD_FOLDER"]/pp_str
    info['file'].save(path)
    
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "INSERT INTO users (username, fullname, email, filename, password, created) VALUES (?, ?, ?, ?, ?, ?)",
        "args": [info['username'], info['name'], info['email'], pp_str, pw_str, timestamp],
    }
    req_hdrs = {
        'content_type': 'application/json'
    }
    get_client().post(req_data, req_hdrs)

    return True


def do_delete():
    """Delete account of logname."""
    # user must be logged in
    if 'logname' not in session:
        abort(403)

    uname = session['logname']

    # delete users entry and all related ones
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "DELETE FROM users WHERE username == ?",
        "args": [uname],
    }
    req_hdrs = {
        'content_type': 'application/json'
    }
    get_client().post(req_data, req_hdrs)

    # clear the session
    session.clear()


def do_update_password(info):
    """Update password with info."""
    if (info['old'] is None or info['new'] is None or
            info['verify_new'] is None):
        abort(400)
    
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT password FROM users WHERE username == ?",
        "args": [info['username']],
    }
    req_hdrs = {
        'content_type': 'application/json'
    }
    old_pw_hash = get_client().get(req_data, req_hdrs)
    old_pw_hash = old_pw_hash[0]

    # check if salt is present (default data isn't encrypted)
    salt = old_pw_hash['password'].split("$")
    if len(salt) > 1:
        salt = salt[1]
        pw_str = model.encrypt(salt, info['old'])
    else:
        pw_str = info['old']
        
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT username FROM users WHERE username == ? AND password == ?",
        "args": [info['username'], pw_str],
    }
    req_hdrs = {
        'content_type': 'application/json'
    }
    user = get_client().get(req_data, req_hdrs)

    if len(user) == 0:
        abort(403)

    if info['new'] != info['verify_new']:
        abort(401)

    new_pw_hash = create_hashed_password(info['new'])
    
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "UPDATE users SET password = ? WHERE username == ?",
        "args": [new_pw_hash, info['username']],
    }
    req_hdrs = {
        'content_type': 'application/json'
    }
    user = get_client().get(req_data, req_hdrs)


@homepage.app.route('/accounts/login/')
def login():
    """Render login page."""
    with homepage.app.app_context():

        # redirect if a session cookie exists
        if 'logname' not in session:
            badlogin = request.args.get("badlogin", type=bool, default=False)
            context = {
                "badlogin": badlogin,
            }
            return render_template("login.html", **context)

        # if there doesn't exist a session cookie,
        # redirect to /accounts/?target=/login/ to create one
        return redirect('/')


@homepage.app.route('/accounts/logout/', methods=['GET'])
def logout():
    """Log out user and redirects to login."""
    session.clear()
    return redirect('/')


def create_hashed_password(pword):
    """Create a hashed password for a new user."""
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + pword
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string


def encrypt(salt, pword):
    """One way decryption given the plaintext pw and salt from user db."""
    algorithm = 'sha512'

    hash_obj = hashlib.new(algorithm)
    password_salted = salt + pword
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string
