from application import db

class Manufacturer(db.Model):
    manID= db.Column(db.Integer, primary_key=True)
    manName = db.Column(db.String(50), nullable=False)
    manSpec = db.Column(db.String(50), nullable=False)
    manLink = db.relationship('Item', backref='manufacturer')

class Item(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    itemColour = db.Column(db.String(50), nullable=False)
    manID = db.Column(db.Integer, db.ForeignKey(Manufacturer.manID))