#!/usr/bin/python3
'''module start a app'''

from flask import Flask

app = Flask('__name__')
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''index page'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''Holberton funtion'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0", port=5000)
