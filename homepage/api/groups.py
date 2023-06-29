import flask
import homepage
from homepage.common.model import get_db, get_logname


@homepage.app.route("/api/v1/groups/upload/")
def upload_group():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.json
    for arg in ["topicId", "groupOrder"]:
        if arg not in body:
            flask.abort(400)

    connection = get_db()

    cur = connection.execute(
        "INSERT INTO groups (owner, topicId, groupOrder)" "VALUES (?, ?, ?)",
        (
            logname,
            body["topicId"],
            body["groupOrder"],
        ),
    )
    cur.fetchone()
    return flask.Response(status=204)


@homepage.app.route("/api/v1/groups/delete/")
def delete_group():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.json
    for arg in ["groupId"]:
        if arg not in body:
            flask.abort(400)

    connection = get_db()

    cur = connection.execute(
        "DELETE FROM groups" "WHERE owner = ? AND groupId = ?",
        (
            logname,
            body["groupId"],
        ),
    )
    cur.fetchone()
    return flask.Response(status=204)
