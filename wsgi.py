#!/bin/python3

import flask
import homepage

app = homepage.app

if __name__ == "__main__":
    app.run(port=8002)
