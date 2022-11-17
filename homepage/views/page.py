import homepage

@homepage.app.route("/p/<page_name>/")
def show_page(page_name: str):
    """Render a created page."""
