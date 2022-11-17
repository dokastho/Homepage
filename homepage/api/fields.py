import homepage

@homepage.app.route("/api/v1/field/update/", methods=["PUT"])
def update_field():
    """Update a text field."""

@homepage.app.route("/api/v1/field/create/", methods=["POST"])
def create_field():
    """Create a text field."""

@homepage.app.route("/api/v1/field/delete/", methods=["DELETE"])
def delete_field():
    """Delete a text field."""

@homepage.app.route("/api/v1/field/fetch/", methods=["PUT"])
def fetch_field():
    """Fetch a text field."""
