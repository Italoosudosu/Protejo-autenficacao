from flask import render_template, request, redirect
from main import app

@app.route("/")
def homepage():
    return render_template ("main.html")


@app.route("/login")
def login():
    return render_template("login.html")
