from sqlalchemy.orm import backref
from application import db

class Item(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    itemColour = db.Column(db.String(50), nullable=False)
    manufacturer = db.relationship('Manufacturer', backref='item')

class Manufacturer(db.Model):
    manID = db.Column(db.Integer, primary_key=True)
    manName = db.Column(db.String(50), nullable=False)
    manSpec = db.Column(db.String(50), nullable=False)