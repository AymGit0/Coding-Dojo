from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo_model
from flask_app.models import ninja_model

# ====== Main Route ========
@app.route("/")
def main():
    return redirect("/dojos")

@app.route("/dojos")
def show_all_dojos():
    dojos = dojo_model.Dojo.all_dojos()

    return render_template("dojos.html", dojos = dojos)

# ====== Action Route ========
@app.route('/dojos/add', methods=['post'])
def process_dojo_form():
    # data = {
    #     'name': request.form['name'],
    #     'population': request.form['population'],
    #     'area': request.form['area']
    # }
    dojo_id = dojo_model.Dojo.create_dojo(request.form)

    return redirect("/dojos")

# ====== Display Route ========
@app.route('/dojos/<int:id>')
def show_one_dojo(id):
    data = {'id':id}
    dojo = dojo_model.Dojo.get_one_dojo_by_id(data)
    ninjas = ninja_model.Ninja.ninjas_dojo(data)

    return render_template("show_dojo.html", dojo = dojo, ninjas = ninjas)