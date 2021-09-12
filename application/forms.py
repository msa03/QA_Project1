from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class itemForm(FlaskForm):
    itemName = StringField("Item Name", validators= [DataRequired()])
    itemColour = StringField("Item Colour", validators= [DataRequired()])
    submit = SubmitField("Submit")

class manForm(FlaskForm):
    manName = StringField("Manufacturer Name", validators= [DataRequired()])
    manSpec = StringField("Manufacturer Specialty", validators= [DataRequired()])
    submit = SubmitField("Add item")