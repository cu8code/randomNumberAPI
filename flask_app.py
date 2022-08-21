from flask import Flask, make_response, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/<username>")
def hello_world(username):
    assert request.method == "GET"
    return f"<p>Hello, {escape(username)}</p>"


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("<p>login page</p>")
    resp.set_cookie('username', 'ankan')
    return resp


@app.route("/get_cookie")
def get_cookie():
    username = request.cookies.get("username")
    return f"is the {username}"


@app.route("/")
def main():
    return {
        "some": "data",
        "xqc": 12,
        "more": {
            "yo": 1
        }
    }
