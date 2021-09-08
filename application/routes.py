from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Items, ItemLists, ItemList_Links
from application.forms import ItemForm, ItemListForm, ItemLinkForm


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title="Shopping List App")

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(
            name = form.name.data,
            quantity = form.quantity.data,
            age_restriction = form.age_restriction.data
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_item.html', title = "Add a new item to your list", form=form)

@app.route('/add_list', methods=['GET', 'POST'])
def add_list()

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
