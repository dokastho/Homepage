import homepage
import flask
import json
from homepage.common.model import get_db, get_logname
from homepage.config import MY_LOGNAME


@homepage.app.route("/api/v1/home/", methods=["GET"])
def fetch_topics_by_owner():
    """Fetch topics for logged in owner."""
    content = dict()
    content["logname"]: get_logname()
    
    owner: str = MY_LOGNAME  # remove me
    content["logname"] = owner  # remove me

    # get topics owned by 'owner'
    connection = get_db()
    
    # topics
    content["topics"] = dict()
    cur = connection.execute("SELECT * FROM topics WHERE owner == ?", (owner,))
    topics = cur.fetchall()
    for topic in topics:
        topic["groups"] = dict()
        topic_id = topic["topicId"]
        content["topics"][topic_id] = topic
        pass
    
    # groups
    cur = connection.execute("SELECT * FROM groups WHERE owner == ?", (owner,))
    groups = cur.fetchall()
    for group in groups:
        group["stories"] = []
        group_id = group["groupId"]
        topic_id = group["topicId"]
        content["topics"][topic_id]["groups"][group_id] = group

    # media
    cur = connection.execute("SELECT * FROM media WHERE owner == ?", (owner,))
    media = cur.fetchall()
    for m in media:
        topic_id = m["topicId"]
        group_id = m["groupId"]
        m["type"] = "media"
        content["topics"][topic_id]["groups"][group_id]["stories"].append(m)
        pass
    # stories
    cur = connection.execute("SELECT * FROM stories WHERE owner == ?", (owner,))
    stories = cur.fetchall()
    for s in stories:
        topic_id = s["topicId"]
        group_id = s["groupId"]
        s["type"] = "story"
        content["topics"][topic_id]["groups"][group_id]["stories"].append(s)
        pass

    return flask.jsonify(content), 201


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
