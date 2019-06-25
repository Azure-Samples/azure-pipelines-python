import simple_package
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    message = request.args.get("message")
    if not message:
        message = "Hello World!"
    return simple_package.echo(message)


@app.route("/shout")
def shout():
    message = request.args.get("message")
    if not message:
        message = "Hello World!"
    return simple_package.shout(message)
