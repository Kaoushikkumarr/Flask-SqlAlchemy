from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ''' defining the app name'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott://tiger@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

""" Declaring the class with same name Exaple which in database. """


class Example(db.Model):  # Declaring the class with same name Example which in database.
    """
    static variable
    """
    __tablename__: str = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)
