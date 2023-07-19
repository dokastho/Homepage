import flask
import homepage
from homepage.common.model import get_logname
from homepage.common.utils import get_group, get_client


@homepage.app.route("/api/v1/groups/get/<groupId>/", methods=["GET"])
def fetch_group(groupId):
    data = get_group(groupId)
    return flask.jsonify(data), 200


@homepage.app.route("/api/v1/groups/update/<groupId>/", methods=["POST"])
def update_group(groupId: int):
    """Update a topic."""

    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "groupOrder" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "UPDATE groups SET groupOrder = ?,name = ? WHERE owner = ? AND groupId = ?",
        "args": [body["groupOrder"], body["name"], logname, groupId],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/groups/upload/", methods=["POST"])
def upload_group():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    body = flask.request.form
    for arg in ["topicId", "name", "groupOrder"]:
        if arg not in body:
            flask.abort(400)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "INSERT INTO groups (owner, name, topicId, groupOrder) VALUES (?, ?, ?)",
        "args": [logname, body["name"], body["topicId"], body["groupOrder"]],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/groups/delete/<groupId>/")
def delete_group(groupId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "DELETE FROM groups WHERE owner = ? AND groupId = ?",
        "args": [logname, groupId],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")
