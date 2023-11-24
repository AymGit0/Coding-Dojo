from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    

users = [
         {"first_name" : "Micheal","last_name" : "Choi" },
         {"first_name" : "John", "last_name" : "Supsupin"},
         {"first_name" : "Mark", "last_name" : "Guillen"},
         {"first_name" : "KB", "last_name" : "Tonel"}

]

@app.route("/")
def home():
    return render_template('index.html',users=users)
if __name__=="__main__":
    app.run(debug=True)   