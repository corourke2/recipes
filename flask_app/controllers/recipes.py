from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.recipe import Recipe

@app.route("/recipes/form")
def recipe_form():
    return render_template("recipe_form.html")

@app.route("/recipes/<int:id>")
def recipe(id):
    data = {
        "id" : id
    }
    recipe = Recipe.get_by_id(data)
    return render_template("recipe.html", recipe = recipe)

@app.route("/recipes/save", methods=["post"])
def save_recipe():
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_made" : request.form["date_made"],
        "under_30" : request.form["under_30"],
        "user_id" : request.form["user_id"]
    }
    Recipe.save(data)
    return redirect("/dashboard")

@app.route("/recipes/<int:id>/edit")
def edit_recipe(id):
    data = {
        "id" : id
    }
    recipe = Recipe.get_by_id(data)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route("/recipes/<int:id>/update", methods=["post"])
def update_recipe(id):
    data = {
        "id" : id,
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_made" : request.form["date_made"],
        "under_30" : request.form["under_30"],
        "user_id" : request.form["user_id"]
    }
    Recipe.update(data)
    return redirect("/dashboard")

@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    data = {
        "id" : id
    }
    Recipe.delete(data)
    return redirect("/dashboard")
