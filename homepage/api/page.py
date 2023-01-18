import homepage
import flask
import json
from homepage.common.model import get_db, get_logname
from homepage.config import MY_LOGNAME


@homepage.app.route("/api/v1/page/update/<pn>/", methods=["PUT"])
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
    if "title" not in body or "description" not in body or "body" not in body or "route" not in body or "card_size":
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)
    
    # create page in db
    cur = connection.execute(
        "UPDATE pages "
        "SET title = ?, description = ?, body = ?, route = ?, card_size = ? "
        "WHERE logname == ? "
        "AND page_id == ?",
        (body["title"], body["description"], body["body"], body["route"], body["card_size"], logname, pn, )
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
    if "title" not in body or "description" not in body or "card_size" not in body:
        flask.abort(400)
    # get user
    logname = get_logname()
    if logname is None:
        flask.abort(403)
    
    # create page in db
    cur = connection.execute(
        "INSERT INTO pages "
        "(title, description, owner, card_size) "
        "VALUES (?, ?, ?, ?)",
        (body["title"], body["description"], body["card_size"], logname, )
    )
    
    cur.fetchone()

    return 201


@homepage.app.route("/api/v1/page/delete/<pn>/", methods=["DELETE"])
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
        "DELETE FROM pages "
        "WHERE page_id == ? ",
        "AND owner == ?"
        (pn, logname, )
    )
    
    cur.fetchone()
    
    return 201


@homepage.app.route("/api/v1/page/fetch/<pn>/", methods=["GET"])
def fetch_page_by_number(pn: int):
    """Fetch a page."""

    return get_page(pn), 201

@homepage.app.route("/api/v1/page/fetchall/", methods=["GET"])
def fetch_page_by_owner():
    """Fetch pages for logged in owner."""
    # if this was a social media site, this would make sense. 
    # So, I'll leave it here on the pretense that it *could*
    # work as a social media site if I had a lot of users or
    # otherwise a lot of site involvement.
    # owner = get_logname()
    # if owner is None:
    #     flask.abort(403)
    # In reality, I just need to display mine
    owner: str = MY_LOGNAME

    # get pages owned by 'owner'
    connection = get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM pages "
        "WHERE owner == ?",
        (owner,)
    )
    
    content = cur.fetchall()

    return content, 201


def get_page(pn: int) -> json:
    """Get page from db. Used more than once so it's a helper."""
    # get page from db & return it
    connection = get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM pages "
        "WHERE page_id == ?",
        (pn,)
    )
    
    page = cur.fetchone()
    if page is None:
        flask.abort(404)
    
    logname = get_logname()
    if logname != page["owner"]:
        flask.abort(403)
    
    return page