"""Render an admin's edit page for one group, topic, story or media"""

import homepage
import flask
from homepage.common.utils import get_topic, get_group, get_story, get_media


@homepage.app.route("/edit/topics/<topicId>/")
def edit_topic(topicId):
    context = get_topic(topicId)

    return flask.render_template("edit-topic.html", **context)


@homepage.app.route("/edit/groups/<groupId>/")
def edit_group(groupId):
    context = get_group(groupId)

    return flask.render_template("edit-group.html", **context)


@homepage.app.route("/edit/stories/<storyId>/")
def edit_story(storyId):
    context = get_story(storyId)

    return flask.render_template("edit-story.html", **context)


@homepage.app.route("/edit/media/<mediaId>/")
def edit_media(mediaId):
    context = get_media(mediaId)

    return flask.render_template("edit-media.html", **context)
