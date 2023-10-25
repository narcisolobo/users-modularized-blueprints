from flask import Blueprint, redirect, render_template, request
from flask_app.models.user import User

users = Blueprint("users", __name__)


@users.get("/")
def index():
    """Redirects the user to /users."""
    return redirect("/users")


@users.get("/users")
def get_all_users():
    """Displays a table showing all users."""
    all_users = User.find_all()
    return render_template("all_users.html", all_users=all_users)


@users.get("/users/new")
def new_user():
    """Displays the new user form."""
    return render_template("new_user.html")


@users.post("/users")
def create_user():
    """Processes the new user form."""
    User.create(request.form)
    return redirect("/users")


@users.get("/users/<int:user_id>")
def get_one_user(user_id):
    """Displays a card showing one user."""
    user = User.find_by_id(user_id)
    return render_template("one_user.html", user=user)


@users.get("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Displays the edit user form."""
    user = User.find_by_id(user_id)
    return render_template("edit_user.html", user=user)


@users.post("/users/update")
def update_user():
    """Processes the edit user form."""
    User.update(request.form)
    return redirect(f'/users/{request.form["id"]}')
