from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.recipe import Recipe

@app.route("/recipes/save", methods=["post"])
def save_recipe():
    return redirect("/dashboard")
