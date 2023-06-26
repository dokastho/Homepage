import homepage
import flask
from homepage.common.model import check_session, get_logname


@homepage.app.route("/")
def show_index():
    """Render homepage for the site."""

    return flask.render_template("index.html")
    # return flask.render_template("wip.html")

@homepage.app.route("/wip/")
def show_wip():
    """Render homepage for the site during development."""

    logname = get_logname()
    if logname is None:
        logname = "log in"
    
    context = dict({"logname": logname})

    return flask.render_template("wip.html", **context)


@homepage.app.route("/user/<uname>/")
def show_user(uname):
    """Show profile options for uname."""
    logname = check_session()
    if not logname:
        return flask.redirect("/accounts/login/")

    if logname != uname:
        return flask.abort(403)

    context = {
        "logname": logname
    }

    return flask.render_template("accounts.html", **context)
