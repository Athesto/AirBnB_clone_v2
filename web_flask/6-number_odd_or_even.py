#!/usr/bin/python3
'''module odd or even'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    '''home path'''
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    '''hbnb path'''
    return "HBNB"


@app.route("/c", strict_slashes=False)
@app.route("/c/<text>")
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>")
def lang(text="is cool"):
    '''print lang'''
    lang = request.path.split('/')[1]
    return "{} {}".format(lang.capitalize(), text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    '''is a number'''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    '''number_template'''
    page = "5-number.html"
    return render_template(page, n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    '''page odd or even'''
    page = "6-number_odd_or_even.html"
    return render_template(page, n=n)


if __name__ == '__main__':
    app.run(host='0', debug=True)
