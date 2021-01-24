from . import app
from flask import render_template, request, redirect, url_for, session
import functools

# from werkzeug.security import check_password_hash

slova = ("Super", "Perfekt", "Úža", "Flask")


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for("login", url=request.path))

    return wrapper

@app.route("/trojuhelnikOS/")
def trojuhelnik():
    title = "Trojuhlnik"
    a = request.args.get("stranaa")
    b = request.args.get("stranab")
    c = request.args.get("stranac")
    try:
        o = int(a) + int(b) + int(c)
    except (TypeError, ValueError):
        o = ''
    return render_template("trojuhelnikOS.html.j2", title=title, o=o)

@app.route("/ctverecOS/")
def ctverec():
    title = "Ctverec"
    a = request.args.get("stranaa")
    try:
        o = 4 * int(a)
        s = int(a) * int(a)
    except (TypeError, ValueError):
        o = ''
        s = ''
    return render_template("ctverecOS.html.j2", title=title, o=o, s=s)

@app.route("/kruhOS/")
def kruh():
    title = "kruh"
    a = request.args.get("a")
    try:
        o = (int(a)*int(a)) * 3.14
        s = int(a) * 2 * 3.14 
    except (TypeError, ValueError):
        o = ''
        s = ''
    return render_template('kruhOS.html.j2', title=title,o=o,s=s)    

@app.route("/obdelnik/")
def obdelnik():
    title = "Obdelnik"
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        o = 2* (int(a)+int(b))
        s = int(a) * int(b)
    except (TypeError, ValueError):
        o = ''
        s = ''
    return render_template("obdelnikOS.html.j2", title=title, o=o, s=s)



@app.route("/", methods=["GET"])
def index():
    return render_template("base.html.j2")


@app.route("/info/")
def info():
    return render_template("info.html.j2")


@app.route("/abc/")
def abc():
    return render_template("abc.html.j2", slova=slova)


@app.route("/text/")
def text():
    return """

<h1>Text</h1>

<p>toto je text</p>

"""
