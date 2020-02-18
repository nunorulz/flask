from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_ERI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.controllers import default
