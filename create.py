from application import db
from application.models import ItemLists, Items, ItemListLinks

db.drop_all()
db.create_all()