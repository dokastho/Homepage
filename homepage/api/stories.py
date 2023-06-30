import flask
import homepage
from homepage.common.model import get_db, get_logname
from homepage.common.utils import get_story


@homepage.app.route("/api/v1/stories/get/<storyId>/", methods=['GET'])
def fetch_story(storyId):
    data = get_story(storyId)
    return flask.jsonify(data), 200


@homepage.app.route("/api/v1/stories/update/<storyId>/", methods=["POST"])
def update_story(storyId: int):
    """Update a topic."""

    connection = get_db()

    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if (
        "storyOrder" not in body or
        "text" not in body
    ):
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    cur = connection.execute(
        "UPDATE stories "
        "SET storyOrder = ?,"
        "text = ?"
        "WHERE owner = ? "
        "AND storyId = ?",
        (
            body["groupOrder"],
            body["text"],
            logname,
            storyId,
        ),
    )

    cur.fetchone()

    return flask.redirect('/admin/')


@homepage.app.route("/api/v1/stories/upload/", methods=['POST'])
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


@homepage.app.route("/api/v1/stories/delete/", methods=['POST'])
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


# @homepage.app.route("/api/v1/stories/delete/", methods=['POST'])