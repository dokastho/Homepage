"""Render an admin's new page for one group, topic, story or media"""

import homepage
import flask


@homepage.app.route("/new/topics/")
def new_topic():
    return flask.render_template("new-topic.html")


@homepage.app.route("/new/groups/")
def new_group():
    context = {
        "topicId": flask.request.args.get("topicId")
    }
    return flask.render_template("new-group.html", **context)


@homepage.app.route("/new/stories/")
def new_story():
    context = {
        "topicId": flask.request.args.get("topicId"),
        "groupId": flask.request.args.get("groupId")
    }
    return flask.render_template("new-story.html", **context)


@homepage.app.route("/new/media/")
def new_media():
    context = {
        "topicId": flask.request.args.get("topicId"),
        "groupId": flask.request.args.get("groupId")
    }
    return flask.render_template("new-media.html", **context)
