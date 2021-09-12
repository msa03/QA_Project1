from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ListForm(FlaskForm):
    list_name = StringField("List Name", validators= [DataRequired()])
    submit = SubmitField("Submit")

class ItemForm(FlaskForm):
    name = StringField("Item Name", validators= [DataRequired()])
    quantity = IntegerField("Item Quantity", default=1)
    submit = SubmitField("Add item")


# class ItemLinkForm(FlaskForm):
#     item = IntegerField("Item ID")
#     itemList = IntegerField("ItemList ID")
#     submit = SubmitField("Add item to list")