import flask
import homepage
import os
from homepage.common.model import get_db, get_logname


@homepage.app.route("/api/v1/media/get/<path:filename>")
def get_image(filename):
    # if 'logname' not in flask.session:
    #     return flask.abort(403)

    return flask.send_from_directory(
        homepage.app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )


@homepage.app.route("/api/v1/media/upload/")
def upload_image(filename):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    fileobj = flask.request.files.get("file")
    if fileobj is None:
        flask.abort(400)
        
    body = flask.request.json
    for arg in ['topicId', 'groupId', 'topicOrder']:
        if arg not in body:
            flask.abort(403)

    # save image
    filename = homepage.model.get_uuid(fileobj.filename)
    path = homepage.app.config["UPLOAD_FOLDER"] / filename
    fileobj.save(path)

    connection = get_db()

    # insert new posts entry
    cur = connection.execute(
        "INSERT INTO media (uuid, owner, topicId, groupId, topicOrder)"
        "VALUES (?, ?, ?, ?, ?)"
        (
            filename,
            logname,
            body['topicId'],
            body['groupId'],
            body['topicOrder'],
        ),
    )
    cur.fetchone()
    return flask.Response(status=204)


@homepage.app.route("/api/v1/media/delete/")
def delete_image():
    logname = get_logname()
    if logname is None:
        flask.abort(403)
    
    body = flask.request.json
    for arg in ['filename', 'mediaId']:
        if arg not in body:
            flask.abort(403)

    # delete image
    path = homepage.app.config["UPLOAD_FOLDER"] / body['filename']
    os.remove(path)

    connection = get_db()

    # insert new posts entry
    cur = connection.execute(
        "DELETE FROM media WHERE logname = ? AND mediaId = ?",
        (
            body['mediaId'],
            logname,
        ),
    )
    cur.fetchone()
    return flask.Response(status=204)
