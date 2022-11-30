import homepage


@homepage.app.route("/api/v1/page/create/", methods=["POST"])
def create_page():
    """Create a page."""


@homepage.app.route("/api/v1/page/delete/", methods=["DELETE"])
def delete_page():
    """Delete a page."""
