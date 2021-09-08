from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Items, ItemLists, ItemList_Links
from application.forms import ItemForm, ItemListForm, ItemLinkForm


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title="Shopping List App")

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    itemform = ItemForm()
    if itemform.validate_on_submit():
        item = Items(
            name = itemform.name.data,
            quantity = itemform.quantity.data,
            age_restriction = itemform.age_restriction.data
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_item.html', title = "Add a new item to your list", form=itemform)

@app.route('/add_list', methods=['GET', 'POST'])
def add_list():
    itemlistform = ItemListForm()
    if itemlistform.validate_on_submit():
        itemList = ItemLists(
            list_name = itemlistform.list_name.data
        )
        db.session.add(itemList)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_list.html', title = "Create a new list", form=itemlistform)

@app.route('/update_item/<id:id>', methods=['GET', 'POST'])
def update_item(id):
    itemform = ItemForm()
    item =Items.query.get(id)
    if itemform.validate_on_submit():
        item.name = itemform.name.data
        db.session.commit()
        redirect(url_for('home'))
    elif request.method == 'GET':
        itemform.name.data = item.name
    return render_template('update.html', title='Update your shopping list', form=itemform)

@app.route('delete/<int:id>')
def delete(id):
    item = Items.query.get(id)
    itemList = ItemLists.query.get(id)
    itemList_link = ItemList_Links.query.get(id)
    db.session.delete(item)
    db.session.delete(itemList)
    db.session.delete(itemList_link)
    db.session.commit()
    return redirect(url_for('home'))
