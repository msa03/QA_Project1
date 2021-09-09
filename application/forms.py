from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Items, ItemLists

class ItemForm(FlaskForm):
    name = StringField("Item Name", validators= [DataRequired()])
    quantity = IntegerField("Item Quantity", default=1)
    age_restriction = SelectField("Age Restriction?",
        choices=[
            (False, "No"),
            (True, "Yes")
        ]
    )
    submit = SubmitField("Add to shopping list")

    def check_item(self, name):
        items = Items.query.all()
        for item in items:
            if item.name == name.data:
                raise ValidationError("This item already exists in your shopping list")

class ItemListForm(FlaskForm):
    list_name = StringField("List Name", validators= [DataRequired()])
    sumbit = SubmitField("Create shopping list")

    def check_itemlist(self, list_name):
        itemLists = ItemLists.query.all()
        for itemList in itemLists:
            if itemList.list_name == list_name.data:
                raise ValidationError("This list already exists - please choose another name")

class ItemLinkForm(FlaskForm):
    item = IntegerField("Item ID")
    itemList = IntegerField("ItemList ID")
    submit = SubmitField("Add item to list")