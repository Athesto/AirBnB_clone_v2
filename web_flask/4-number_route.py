#!/usr/bin/python3
'''module is a number'''

from flask import Flask, request
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''index route'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''hbnb'''
    return "HBNB"


@app.route('/c')
@app.route('/c/<text>')
@app.route('/python')
@app.route('/python/<text>')
def lang(text="is_cool"):
    '''lang are fun'''
    lang = request.path.split('/')[1]
    return "{} {}".format(lang.capitalize(), text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    '''it's a number'''
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0", debug=True)
