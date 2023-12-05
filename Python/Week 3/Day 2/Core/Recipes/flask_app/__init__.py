# __init__.py
from flask import Flask

app = Flask(__name__)
app.secret_key = "1234"
DATABASE = "recipes_schema"