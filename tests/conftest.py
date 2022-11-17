import pytest
import canvasapi
import subprocess


@pytest.fixture(name="client")
def client_setup_teardown():
    """
    Start a Flask test server with a clean database.

    This fixture is used to test the REST API, it won't start a live server.

    Flask docs: https://flask.palletsprojects.com/en/1.1.x/testing/#testing
    """

    # Configure Flask test server
    canvasapi.app.config["TESTING"] = True

    # Transfer control to test.  The code before the "yield" statement is setup
    # code, which is executed before the test.  Code after the "yield" is
    # teardown code, which is executed at the end of the test.  Teardown code
    # is executed whether the test passed or failed.
    with canvasapi.app.test_client() as client:
        yield client
