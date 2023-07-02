import flask
import homepage
from homepage.common.model import get_db, get_logname
from homepage.common.utils import get_group


@homepage.app.route("/api/v1/groups/get/<groupId>/", methods=["GET"])
def fetch_group(groupId):
    data = get_group(groupId)
    return flask.jsonify(data), 200


@homepage.app.route("/api/v1/groups/update/<groupId>/", methods=["POST"])
def update_group(groupId: int):
    """Update a topic."""

    connection = get_db()

    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if (
        "groupOrder" not in body
    ):
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    cur = connection.execute(
        "UPDATE groups "
        "SET groupOrder = ?,"
        "name = ? "
        "WHERE owner = ? "
        "AND groupId = ?",
        (
            body["groupOrder"],
            body["name"],
            logname,
            groupId,
        ),
    )

    cur.fetchone()

    return flask.redirect('/admin/')


@homepage.app.route("/api/v1/groups/upload/", methods=["POST"])
def upload_group():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.form
    for arg in ["topicId", "name", "groupOrder"]:
        if arg not in body:
            flask.abort(400)

    connection = get_db()

    cur = connection.execute(
        "INSERT INTO groups (owner, name, topicId, groupOrder)" "VALUES (?, ?, ?)",
        (
            logname,
            body["name"],
            body["topicId"],
            body["groupOrder"],
        ),
    )
    cur.fetchone()
    return flask.redirect('/admin/')


@homepage.app.route("/api/v1/groups/delete/<groupId>/")
def delete_group(groupId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    connection = get_db()

    cur = connection.execute(
        "DELETE FROM groups WHERE owner = ? AND groupId = ?",
        (
            logname,
            groupId,
        ),
    )
    cur.fetchone()
    return flask.redirect('/admin/')
