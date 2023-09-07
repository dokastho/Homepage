import flask
from homepage.config import MY_LOGNAME
import homepage
from random import randint
from d3b_client.client import *


def get_client(host_id: int = 0) -> d3b_client:
    # if "FLASK_DEBUG" in os.environ.keys():
    #     return d3b_client("https://dev2.dokastho.io")
    if host_id == 0:
        host_id = randint(1, homepage.app.config["NDBS"])
        pass

    hostname = f"https://d3b{host_id}.dokastho.io"
    c = d3b_client(hostname)
    return c


def get_all():
    content = dict()
    content["logname"]: homepage.common.model.get_logname()

    owner: str = MY_LOGNAME  # remove me
    content["logname"] = owner  # remove me

    # get topics owned by 'owner'

    # topics
    content["topics"] = dict()

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM topics WHERE owner == ?",
        "args": [owner],
    }
    req_hdrs = {"content_type": "application/json"}
    topics = get_client(1).get(req_data, req_hdrs)

    for topic in topics:
        topic["groups"] = dict()
        topic_id = topic["topicId"]
        content["topics"][topic_id] = topic
        pass

    # groups
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM groups WHERE owner == ?",
        "args": [owner],
    }
    req_hdrs = {"content_type": "application/json"}
    groups = get_client(2).get(req_data, req_hdrs)

    for group in groups:
        group["stories"] = []
        group_id = group["groupId"]
        topic_id = group["topicId"]
        content["topics"][topic_id]["groups"][group_id] = group

    # media
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM media WHERE owner == ?",
        "args": [owner],
    }
    req_hdrs = {"content_type": "application/json"}
    media = get_client(3).get(req_data, req_hdrs)

    for m in media:
        topic_id = m["topicId"]
        group_id = m["groupId"]
        m["type"] = "media"
        content["topics"][topic_id]["groups"][group_id]["stories"].append(m)
        pass
    # stories
    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM stories WHERE owner == ?",
        "args": [owner],
    }
    req_hdrs = {"content_type": "application/json"}
    stories = get_client(1).get(req_data, req_hdrs)

    for s in stories:
        topic_id = s["topicId"]
        group_id = s["groupId"]
        s["type"] = "story"
        content["topics"][topic_id]["groups"][group_id]["stories"].append(s)
        pass
    return content


def get_topic(topicId):
    logname = homepage.common.model.get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM topics WHERE topicId = ? AND owner = ?",
        "args": [topicId, logname],
    }
    req_hdrs = {"content_type": "application/json"}
    data = get_client().get(req_data, req_hdrs)

    return data[0]


def get_group(groupId):
    logname = homepage.common.model.get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM groups WHERE groupId = ? AND owner = ?",
        "args": [groupId, logname],
    }
    req_hdrs = {"content_type": "application/json"}
    data = get_client().get(req_data, req_hdrs)

    return data[0]


def get_story(storyId):
    logname = homepage.common.model.get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM stories WHERE storyId = ? AND owner = ?",
        "args": [storyId, logname],
    }
    req_hdrs = {"content_type": "application/json"}
    data = get_client().get(req_data, req_hdrs)

    return data[0]


def get_media(mediaId):
    logname = homepage.common.model.get_logname()
    if logname is None:
        flask.abort(403)

    req_data = {
        "table": homepage.app.config["DATABASE_FILENAME"],
        "query": "SELECT * FROM media WHERE mediaId = ? AND owner = ?",
        "args": [mediaId, logname],
    }
    req_hdrs = {"content_type": "application/json"}
    data = get_client().get(req_data, req_hdrs)

    return data[0]
