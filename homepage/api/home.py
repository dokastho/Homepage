import homepage
import flask
from homepage.common.utils import get_all


@homepage.app.route("/api/v1/home/", methods=["GET"])
def fetch_index_state():
    """Fetch topics for logged in owner."""
    content = get_all()

    return flask.jsonify(content), 201
