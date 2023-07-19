import flask
import homepage
from homepage.common.model import get_logname
from homepage.common.utils import get_story, get_client


@homepage.app.route("/api/v1/stories/get/<storyId>/", methods=["GET"])
def fetch_story(storyId):
    data = get_story(storyId)
    return flask.jsonify(data), 200


@homepage.app.route("/api/v1/stories/update/<storyId>/", methods=["POST"])
def update_story(storyId: int):
    """Update a topic."""

    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "storyOrder" not in body or "text" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "UPDATE stories SET storyOrder = ?, text = ? WHERE owner = ? AND storyId = ?",
        "args": [body["storyOrder"], body["text"], logname, storyId],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/stories/upload/", methods=["POST"])
def upload_story():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.form
    for arg in ["text", "topicId", "groupId", "storyOrder"]:
        if arg not in body:
            flask.abort(400)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "INSERT INTO stories (text, owner, topicId, groupId, storyOrder) VALUES (?, ?, ?, ?, ?)",
        "args": [
            body["text"],
            logname,
            body["topicId"],
            body["groupId"],
            body["storyOrder"]
        ],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/stories/delete/<storyId>/")
def delete_story(storyId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "DELETE FROM stories WHERE owner == ? AND storyId == ?",
        "args": [logname, storyId],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")
