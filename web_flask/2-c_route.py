#!/usr/bin/python3
'''module that starts a Flask web application'''

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''index page'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''hbnb page'''
    return "HBNB"


@app.route('/c/<message>')
def c(message):
    '''c page'''
    return "C {}".format(message.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0", port=5000)
