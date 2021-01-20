#!/usr/bin/python3
'''module hello-route'''

from flask import Flask
app = Flask('__name__')
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''root of server'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0', port=5000)
