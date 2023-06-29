import flask
import homepage
from homepage.common.model import get_db, get_logname


@homepage.app.route("/api/v1/stories/upload/")
def upload_story():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.json
    for arg in ["text", "topicId", "groupId", "topicOrder"]:
        if arg not in body:
            flask.abort(400)

    connection = get_db()

    cur = connection.execute(
        "INSERT INTO stories (text, owner, topicId, groupId, topicOrder)"
        "VALUES (?, ?, ?, ?, ?)",
        (
            body["text"],
            logname,
            body["topicId"],
            body["groupId"],
            body["topicOrder"],
        ),
    )
    cur.fetchone()
    return flask.Response(status=204)


@homepage.app.route("/api/v1/stories/delete/")
def delete_story():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.json

    connection = get_db()

    cur = connection.execute(
        "DELETE FROM groups" "WHERE owner = ? AND storyId = ?",
        (
            logname,
            body["storyId"],
        ),
    )
    cur.fetchone()
    return flask.Response(status=204)
