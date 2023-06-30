import homepage
import flask
from homepage.common.model import get_db, get_logname
from homepage.config import MY_LOGNAME


@homepage.app.route("/api/v1/home/", methods=["GET"])
def fetch_index_state():
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
