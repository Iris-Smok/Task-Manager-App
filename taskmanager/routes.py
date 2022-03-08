"""
routes.py
"""
from flask import render_template, request, redirect, url_for
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
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    When user click to add a new category it should render
    the template that contains a form. And by displaying the form to users
    this uses the GET method to get the page. Whrn user submits this form,
    the form will attempt to post the data into the database.
    This is why we need to specify both methods in the app route
    """
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    edit_category.html
    """
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    """
    delete categories
    """
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))
