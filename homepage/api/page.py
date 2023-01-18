import homepage
import flask
import json
from homepage.common.model import get_db, get_logname


@homepage.app.route("/api/v1/page/update/", methods=["PUT"])
def update_page(pn: int):
    """Update a page."""
    # function will abort if the page doesn't exist
    get_page(pn)
    
    connection = get_db()
        
    # get values from body
    body = flask.request.get_json()
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "title" not in body or "description" not in body or "body" not in body or "route" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)
    
    # create page in db
    cur = connection.execute(
        "UPDATE pages"
        "SET title = ?, description = ?, body = ?, route = ?"
        "WHERE logname == ?"
        "AND pageid == ?",
        (body["title"], body["description"], body["body"], body["route"], logname, pn, )
    )
    
    cur.fetchone()

    return 201


@homepage.app.route("/api/v1/page/create/", methods=["POST"])
def create_page():
    """Create a page."""
    connection = get_db()
    
    # get values from body
    body = flask.request.get_json()
    # body extists?
    if body is None:
        flask.abort(400)
    # fields in body?
    if "title" not in body or "description" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)
    
    # create page in db
    cur = connection.execute(
        "INSERT INTO pages"
        "(title, description, owner)"
        "VALUES (?, ?, ?)",
        (body["title"], body["description"], logname, )
    )
    
    cur.fetchone()

    return 201


@homepage.app.route("/api/v1/page/delete/", methods=["DELETE"])
def delete_page(pn: int):
    """Delete a page."""
    # function will abort if the page doesn't exist
    get_page(pn)
    
    connection = get_db()
    
    logname = get_logname()
    if logname is None:
        flask.abort(403)

    # delete page from db
    cur = connection.execute(
        "DELETE FROM pages"
        "WHERE pageid == ?",
        "AND owner == ?"
        (pn, logname, )
    )
    
    cur.fetchone()
    
    return 201


@homepage.app.route("/api/v1/page/fetch/<pn>", methods=["GET"])
def fetch_page(pn: int):
    """Fetch a page."""

    return get_page(pn), 201



def get_page(pn: int) -> json:
    """Get page from db. Used more than once so it's a helper."""
    # get page from db & return it
    connection = get_db()
    cur = connection.execute(
        "SELECT *"
        "FROM pages"
        "WHERE pageid == ?",
        (pn,)
    )
    
    page = cur.fetchone()
    if page is None:
        flask.abort(404)
    
    logname = get_logname()
    if logname != page["owner"]:
        flask.abort(403)
    
    return page