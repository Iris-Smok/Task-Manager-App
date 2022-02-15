"""
routes.py
"""
from flask import render_template
from taskmanager import app, db  # noqa
from taskmanager.models import Category, Task  # noqa


@app.route("/")
def home():
    """
    home page, when user visit our site, they're
    brought to the tasks page
    """
    return render_template("tasks.html")
