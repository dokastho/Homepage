import homepage
import flask
import json
from homepage.common.model import get_db, get_logname
from homepage.common.utils import get_topic


@homepage.app.route("/api/v1/topics/get/<topicId>/", methods=["GET"])
def fetch_topic(topicId):
    data = get_topic(topicId)
    return flask.jsonify(data), 200


@homepage.app.route("/api/v1/topics/update/<topicId>/", methods=["POST"])
def update_topic(topicId: int):
    """Update a topic."""

    connection = get_db()

    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "name" not in body or "icon" not in body or "styles" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    cur = connection.execute(
        "UPDATE topics "
        "SET name = ?,"
        "icon = ?,"
        "styles = ?"
        "WHERE owner = ? "
        "AND topicId = ?",
        (
            body["name"],
            body["icon"],
            body["styles"],
            logname,
            topicId,
        ),
    )

    cur.fetchone()

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/topics/upload/", methods=["POST"])
def create_topic():
    """Create a topic."""
    connection = get_db()

    # get values from body
    body = flask.request.form
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "name" not in body or "styles" not in body or "icon" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    # create topic in db
    cur = connection.execute(
        "INSERT INTO topics (name, owner, styles, icon) VALUES (?, ?, ?, ?)",
        (
            body["name"],
            logname,
            body["styles"],
            body["icon"],
        ),
    )

    cur.fetchone()

    return flask.redirect("/admin/")


@homepage.app.route("/api/v1/topics/delete/<topicId>/")
def delete_topic(topicId: int):
    """Delete a topic."""

    connection = get_db()

    logname = get_logname()
    if logname is None:
        flask.abort(403)

    # delete topic from db
    cur = connection.execute(
        "DELETE FROM topics WHERE topicId == ? AND owner == ?",
        (
            topicId,
            logname,
        ),
    )

    cur.fetchone()

    return flask.redirect("/admin/")
