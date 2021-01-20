#!/usr/bin/python3
'''module flask app default'''

from flask import Flask, request
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    '''index'''
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c")
@app.route("/c/<message>")
@app.route("/python")
@app.route("/python/<message>")
def lang(message="is_cool"):
    lang = request.path.split('/')[1]
    return "{} {}".format(lang.capitalize(), message.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0", debug=False)
