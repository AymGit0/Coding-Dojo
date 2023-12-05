from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import ninja_model
from flask_app.models import dojo_model

# ======= Display Route ========
@app.route("/ninjas")
def all_ninjas():
    all_ninjas = ninja_model.Ninja.all_ninjas()
    return render_template("ninjas.html", all_ninjas = all_ninjas)

# Display Route
@app.route("/ninjas/new")
def display_ninja_form():
    all_dojos = dojo_model.Dojo.all_dojos()
    print(all_dojos)
    return render_template("create_ninjas.html", all_dojos = all_dojos)


# Action Route 
@app.route("/process", methods=['post'])
def ninja():
    ninja_model.Ninja.create_ninja(request.form)
    return redirect("/dojos")