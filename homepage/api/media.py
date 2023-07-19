import flask
import homepage
import os
from homepage.common.model import get_logname
from homepage.common.utils import get_client


@homepage.app.route("/api/v1/media/get/<path:filename>/")
def get_image(filename):
    # if 'logname' not in flask.session:
    #     return flask.abort(403)

    return flask.send_from_directory(
        homepage.app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )


@homepage.app.route("/api/v1/media/update/<mediaId>/", methods=["POST"])
def update_media(mediaId):
    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "storyOrder" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "UPDATE media SET storyOrder = ?WHERE owner = ? AND mediaId = ?",
        "args": [body["storyOrder"], logname, mediaId],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/media/upload/", methods=["POST"])
def upload_image():
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    fileobj = flask.request.files.get("file")
    if fileobj is None:
        flask.abort(400)

    body = flask.request.form
    for arg in ["topicId", "groupId", "storyOrder"]:
        if arg not in body:
            flask.abort(403)

    # save image
    filename = homepage.common.model.get_uuid(fileobj.filename)
    path = homepage.app.config["UPLOAD_FOLDER"] / filename
    fileobj.save(path)

    # insert new posts entry
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "INSERT INTO media (uuid, owner, topicId, groupId, storyOrder) VALUES (?, ?, ?, ?, ?)",
        "args": [
            filename,
            logname,
            body["topicId"],
            body["groupId"],
            body["storyOrder"],
        ],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/media/delete/<mediaId>/")
def delete_image(mediaId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    filename = flask.request.args.get("filename")
    if filename is None:
        flask.abort(400)

    # delete image
    path = homepage.app.config["UPLOAD_FOLDER"] / filename
    os.remove(path)

    # insert new posts entry
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "DELETE FROM media WHERE owner = ? AND mediaId = ?",
        "args": [logname, mediaId],
    }
    req_hdrs = {"content_type": "application/json"}
    get_client().post(req_data, req_hdrs)

    return flask.redirect("/admin/")
