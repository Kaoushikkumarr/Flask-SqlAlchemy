"""
Defining one to many relationship
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

''' creating the object'''
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott://tiger@localhost/mydatabase'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

""" Creating class Person."""


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    pets = db.relationship('Pet', backref='owner')


""" Creating Pet class which is the child class of Person. """


class Pet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
