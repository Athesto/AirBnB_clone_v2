#!/usr/bin/python3
'''module flask app default'''

from flask import Flask
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
def c(message="is_fun"):
    return "C {}".format(message.replace("_", " "))


@app.route("/python")
@app.route("/python/<message>")
def python(message="is_fun"):
    return "python {}".format(message.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0", debug=False)
