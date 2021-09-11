from enum import unique
from sqlalchemy.orm import backref
from application import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    listlink1 = db.relationship('ItemListLinks', backref=db.backref('item'))

class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), nullable=False)
    listlink2 = db.relationship('ItemListLinks', backref=db.backref('list'))

class ItemListLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    fk_itemList_id = db.Column(db.Integer, db.ForeignKey('lists.id'))