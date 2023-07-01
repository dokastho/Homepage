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
            body["storyOrder"],
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

    body = flask.request.form
    for arg in ["text", "topicId", "groupId", "storyOrder"]:
        if arg not in body:
            flask.abort(400)

    connection = get_db()

    cur = connection.execute(
        "INSERT INTO stories (text, owner, topicId, groupId, storyOrder)"
        "VALUES (?, ?, ?, ?, ?)",
        (
            body["text"],
            logname,
            body["topicId"],
            body["groupId"],
            body["storyOrder"],
        ),
    )
    cur.fetchone()
    return flask.redirect('/admin/')


@homepage.app.route("/api/v1/stories/delete/<storyId>/")
def delete_story(storyId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    connection = get_db()

    cur = connection.execute(
        "DELETE FROM stories WHERE owner == ? AND storyId == ?",
        (
            logname,
            storyId,
        ),
    )
    cur.fetchone()
    return flask.redirect('/admin/')
