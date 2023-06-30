"""Render an admin's status page for groups, topics, stories & media"""

import homepage
import flask
from homepage.common.model import get_logname
from homepage.common.utils import get_all


@homepage.app.route("/admin/")
def show_admin_panel():
    logname = get_logname()
    if logname is None:
        return flask.redirect("/accounts/login/")

    context = get_all()
    
    return flask.render_template("admin.html", **context)
    
    