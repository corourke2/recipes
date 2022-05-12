import bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

bcrypt = Bcrypt(app)

@app.route("/")
def login_and_reg():
    return render_template("index.html")

@app.route("/users/register", methods=["post"])
def register():
    if not User.validate_registration(request.form):
        return redirect("/")
    user_id = User.save(request.form)
    session["id"] = user_id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if not "user_id" in session:
        return redirect("/")
    user = User.get_by_id(session["id"])
    recipes = Recipe.get_all()
    return render_template("dashboard.html", user = user, recipes = recipes)

@app.route("/users/login", methods=["post"])
def login():
    if not User.validate_login:
        return redirect("/")
    form_data = {
        "email" : request.form["email"]
    }
    user = User.get_by_email(form_data)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            flash("Incorrect email/password combination")
            return redirect("/")
        session["id"] = user["id"] 
        return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")