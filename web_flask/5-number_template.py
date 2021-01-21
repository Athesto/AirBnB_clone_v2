#!/usr/bin/python3
'''module with templates'''
from flask import Flask, request, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    '''home path'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''simple print'''
    return "HBNB"


@app.route('/c')
@app.route('/c/<text>')
@app.route('/python')
@app.route('/python/<text>')
def lang(text="is cool"):
    '''lang'''
    lang = request.path.split('/')[1]
    return "{} {}".format(lang.capitalize(), text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    '''is a number'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''template number page'''
    page = "5-number.html"
    return render_template(page, n=n)


if __name__ == '__main__':
    app.run(host='0', debug=False)
