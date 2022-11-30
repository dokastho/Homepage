"""accounts interface."""
import uuid
import hashlib
import os
import arrow
from flask import abort, redirect, render_template, request, session
import homepage


@homepage.app.route('/accounts/', methods=['POST'])
def accounts():
    """/accounts/?target=URL Immediate redirect. No screenshot."""
    with homepage.app.app_context():
        connection = homepage.model.get_db()

        # check if target is unspecified or blank
        target = homepage.model.get_target()

        # get operation
        operation = request.form.get('operation')

        # create a login cookie
        if operation == "login":

            # get username and password from form
            uname = request.form['username']
            pword = request.form['password']

            # set session cookie
            if not do_login(uname, pword):
                abort(500)      # server didn't abort
            session['logname'] = uname

        # do not allow creating or deleting without being logged in
        elif 'logname' not in session:
            abort(403)

        # create an account
        elif operation == "create":
            info = {
                "username": request.form.get("username"),
                "email": request.form.get("email"),
                "password": request.form.get("password")
            }
            if not do_create(connection, info):
                abort(500)      # server didn't abort correctly

        elif operation == "delete":
            do_delete(connection)

        elif operation == "update_password":
            # user must be logged in
            if 'logname' not in session:
                abort(403)

            info = {
                "username": session['logname'],
                "old": request.form.get('oldpw'),
                "new": request.form.get("newpw"),
                "verify_new": request.form.get("renewpw"),
            }
            do_update_password(connection, info)

        else:
            abort(400)  # invalid request

    return redirect(target)


def do_login(uname, pword):
    """Login user with username and password."""
    logname = homepage.model.check_authorization(uname, pword)
    if not logname:
        abort(403)

    return True


def do_create(connection, info):
    """Create account with info."""
    for i in info:
        if i == "":
            abort(400)

    utc = arrow.utcnow()
    local = utc.to('US/Pacific')
    timestamp = local.format()

    pw_str = create_hashed_password(info['password'])

    cur = connection.execute(
        "SELECT username "
        "FROM users "
        "WHERE username == ? ",
        (info['username'],)
    )
    user = cur.fetchall()
    if len(user) != 0:
        abort(409)

    cur = connection.execute(
        "INSERT INTO users "
        "(username, email, password, created) "
        "VALUES (?, ?, ?, ?)",
        (
            info['username'], info['email'], pw_str, timestamp,
        )
    )
    cur.fetchall()

    return True


def do_delete(connection):
    """Delete account of logname."""
    # user must be logged in
    if 'logname' not in session:
        abort(403)

    uname = session['logname']

    # delete users entry and all related ones
    cur = connection.execute(
        "DELETE FROM users "
        "WHERE username == ?",
        (uname,)
    )
    cur.fetchall()

    # clear the session
    session.clear()


def do_update_password(connection, info):
    """Update password with info."""
    if (info['old'] is None or info['new'] is None or
            info['verify_new'] is None):
        abort(400)

    cur = connection.execute(
        "SELECT password "
        "FROM users "
        "WHERE username == ? ",
        (info['username'],)
    )
    old_pw_hash = cur.fetchall()
    old_pw_hash = old_pw_hash[0]

    # check if salt is present (default data isn't encrypted)
    salt = old_pw_hash['password'].split("$")
    if len(salt) > 1:
        salt = salt[1]
        pw_str = homepage.model.encrypt(salt, info['old'])
    else:
        pw_str = info['old']

    cur = connection.execute(
        "SELECT username "
        "FROM users "
        "WHERE username == ? "
        "AND password == ?",
        (info['username'], pw_str,)
    )
    user = cur.fetchall()
    if len(user) == 0:
        abort(403)

    if info['new'] != info['verify_new']:
        abort(401)

    new_pw_hash = create_hashed_password(info['new'])
    cur = connection.execute(
        "UPDATE users "
        "SET password = ? "
        "WHERE username == ? ",
        (new_pw_hash, info['username'],)
    )
    user = cur.fetchall()


@homepage.app.route('/accounts/login/')
def login():
    """Render login page."""
    with homepage.app.app_context():

        # redirect if a session cookie exists
        if 'logname' not in session:
            return render_template("login.html")

        # if there doesn't exist a session cookie,
        # redirect to /accounts/?target=/login/ to create one
        return redirect('/')


@homepage.app.route('/accounts/logout/', methods=['POST'])
def logout():
    """Log out user and redirects to login."""
    session.clear()
    return redirect('/')


@homepage.app.route('/accounts/create/', methods=['GET'])
def create():
    """Render create page if not logged in."""

    return render_template('create.html')


@homepage.app.route('/accounts/delete/')
def delete():
    """Render delete page if logged in."""
    if 'logname' not in session:
        abort(403)

    context = {
        "logname": session['logname']
    }
    return render_template('delete.html', **context)


@homepage.app.route('/accounts/password/')
def password():
    """Render page to update password if logged in."""
    if 'logname' not in session:
        abort(403)
    context = {
        "logname": session['logname']
    }
    return render_template('password.html', **context)


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
