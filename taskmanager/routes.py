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


@app.route("/categories")
def categories():
    """
    Categories.html
    """
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    When user click to add a new category it should render
    the template that contains a form. And by displaying the form to users
    this uses the GET method to get the page. Whrn user submits this form,
    the form will attempt to post the data into the database.
    This is why we need to specify both methods in the app route
    """
    return render_template("add_category.html")
