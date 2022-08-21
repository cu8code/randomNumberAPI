from flask import Flask
from makeupsafe import escape

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return f"<p>Hello, {escape(name)}</p>"
