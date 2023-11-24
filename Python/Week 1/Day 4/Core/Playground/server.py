from flask import Flask, render_template , url_for , redirect

app = Flask(__name__)

@app.route("/")
def home(): 
    return redirect("/play")

@app.route("/play")
def home_a(): 
    return render_template("index.html" , num = 1)

@app.route("/play/<number>")
def play(number):
    return render_template("index.html" , num=number)

@app.route("/play/<number>/<color>")
def changecol(number , color):
    return render_template("index.html" , num=number , myCol=color)

if __name__=="__main__":    
    app.run(debug=True) 
