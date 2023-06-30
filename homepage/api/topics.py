import homepage
import flask
import json
from homepage.common.model import get_db, get_logname
from homepage.common.utils import get_topic


@homepage.app.route("/api/v1/topics/get/<topicId>/", methods=['GET'])
def fetch_topic(topicId):
    data = get_topic(topicId)
    return flask.jsonify(data), 200


@homepage.app.route("/api/v1/topic/update/<tn>/", methods=["PUT"])
def update_topic(tn: int):
    """Update a topic."""
    # function will abort if the page doesn't exist
    get_topic(tn)

    connection = get_db()

    # get values from body
    body = flask.request.get_json()
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if (
        "title" not in body
        or "description" not in body
        or "body" not in body
        or "route" not in body
    ):
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    # create page in db
    cur = connection.execute(
        "UPDATE topics "
        "SET title = ?, description = ?, body = ?, route = ?"
        "WHERE logname == ? "
        "AND topicId == ?",
        (
            body["title"],
            body["description"],
            body["body"],
            body["route"],
            logname,
            tn,
        ),
    )

    cur.fetchone()

    return 201


@homepage.app.route("/api/v1/topic/create/", methods=["POST"])
def create_topic():
    """Create a topic."""
    connection = get_db()

    # get values from body
    body = flask.request.get_json()
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "title" not in body or "description" not in body or "topicId" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    # create topic in db
    cur = connection.execute(
        "INSERT INTO topics "
        "(title, description, owner, topicId) "
        "VALUES (?, ?, ?, ?)",
        (
            body["title"],
            body["description"],
            logname,
            body["topicId"],
        ),
    )

    cur.fetchone()

    return flask.Response(status=201)


@homepage.app.route("/api/v1/topic/delete/<tn>/", methods=["DELETE"])
def delete_topic(tn: int):
    """Delete a topic."""
    # function will abort if the page doesn't exist
    get_topic(tn)

    connection = get_db()

    logname = get_logname()
    if logname is None:
        flask.abort(403)

    # delete topic from db
    cur = connection.execute(
        "DELETE FROM topics " "WHERE topicId == ? ",
        "AND owner == ?",
        (
            tn,
            logname,
        ),
    )

    cur.fetchone()

    return flask.Response(status=201)


@homepage.app.route("/api/v1/topic/fetch/<tn>/", methods=["GET"])
def fetch_page_by_number(tn: int):
    """Fetch a topic."""

    return flask.jsonify(get_topic(tn)), 201


def get_topic(pn: int) -> json:
    """Get topic from db. Used more than once so it's a helper."""
    connection = get_db()
    cur = connection.execute("SELECT * " "FROM topics " "WHERE topcId == ?", (pn,))

    topic = cur.fetchone()
    if topic is None:
        flask.abort(404)

    logname = get_logname()
    if logname != topic["owner"]:
        pass
        # once again, this is only relevant if this were a true multi-user site
        # with user-specific content
        # flask.abort(403)

    return topic
