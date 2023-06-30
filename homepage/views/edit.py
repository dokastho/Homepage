"""Render an admin's edit page for one group, topic, story or media"""

import homepage
import flask
from homepage.common.model import get_logname
from homepage.common.utils import get_topic


@homepage.app.route("/edit/topic/<topicId>/")
def edit_topic(topicId):
    context = get_topic(topicId)

    return flask.render_template("edit-topic.html")


@homepage.app.route("/edit/group/<groupId>/")
def edit_group(groupId):
    context = get_topic(groupId)

    return flask.render_template("edit-group.html")


@homepage.app.route("/edit/story/<storyId>/")
def edit_story(storyId):
    context = get_topic(storyId)

    return flask.render_template("edit-story.html")
