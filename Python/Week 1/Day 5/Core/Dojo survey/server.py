from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results', methods =['POST'])
def myResult():
    
    name = request.form['userName']
    location = request.form['userLocation']
    language = request.form['userLanguage']
    comment = request.form['userComment']
    
    return render_template("results.html", name=request.form['userName'], location=request.form['userLocation'], language = request.form['userLanguage'], comment = request.form['userComment'])

app.run(debug=True)

