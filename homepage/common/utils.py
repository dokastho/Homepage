import flask
from homepage.common.model import get_db, get_logname


def get_topic(topicId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)
        
    connection = get_db()

    cur = connection.execute(
        "SELECT * FROM topics WHERE topicId = ? AND owner = ?",
        (
            topicId,
            logname,
        ),
    )
    data = cur.fetchone()
    return data


def get_group(groupId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    connection = get_db()

    cur = connection.execute(
        "SELECT * FROM groups WHERE groupId = ? AND owner = ?",
        (
            groupId,
            logname,
        ),
    )
    data = cur.fetchone()
    return data


def get_story(storyId):
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    connection = get_db()

    cur = connection.execute(
        "SELECT * FROM stories WHERE storyId = ? AND owner = ?",
        (
            storyId,
            logname,
        ),
    )
    data = cur.fetchone()
    return data