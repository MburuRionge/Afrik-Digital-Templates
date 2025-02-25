from flask import render_template, request, Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,
import os


app = Flask(__name__)
electrical = Blueprint('electrical', __name__)

@app.route('/')
def index():
    render_template('index.html')