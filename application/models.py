from enum import unique
from sqlalchemy.orm import backref
from application import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer)
    age_restriction = db.Column(db.Boolean, default=False)
    itemList_link = db.relationship("ItemList_Links", backref="item")

class ItemLists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), nullable=False)
    itemList_link = db.relationship("ItemList_Links", backref="itemList")

class ItemList_Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_item_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))
    fk_itemList_id = db.Column("itemLists_id", db.Integer, db.ForeignKey("itemLists.id"))