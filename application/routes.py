from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Items, Lists, ItemListLinks
from application.forms import ItemForm, ListForm, ItemLinkForm


@app.route('/')
@app.route('/read', methods=['GET', 'POST'])
def read():
    form = ItemForm()
    items = Items.query.all()
    return render_template('home.html', title="Home", items=items, form=form)

@app.route('/add-list', methods=['GET', 'POST'])
def add_list():
    form = ListForm()
    if form.validate_on_submit():
        new_list = Lists(
            list_name = form.list_name.data
        )
        db.session.add(new_list)
        db.session.commit()
        return redirect(url_for('add_item'))
    return render_template('add_list.html', title = "Create new list", form=form)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Items(
            name = form.name.data,
            quantity = form.quantity.data,
            )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('add_item.html', title = "Add new item to list", form=form)

@app.route('/update-item', methods=['GET', 'POST'])
def update_item():
    itemform = ItemForm()
    # item =Items.query.get(id)
#     if itemform.validate_on_submit():
#         item.name = itemform.name.data
#         db.session.commit()
#         redirect(url_for('home'))
#     elif request.method == 'GET':
#         itemform.name.data = item.name
    return render_template('update.html', title='Update item', form=itemform)

@app.route('/update-list', methods=['GET', 'POST'])
def update_list():
    itemlistform = ListForm()
    # itemList =ItemLists.query.get(id)
#     if itemlistform.validate_on_submit():
#         itemList.name = itemlistform.name.data
#         db.session.commit()
#         redirect(url_for('home'))
#     elif request.method == 'GET':
#         itemlistform.name.data = itemList.name
    return render_template('update.html', title='Update shopping list name', form=itemlistform)

@app.route('/delete-item')
def delete_item():
    # item = Items.query.get(id)
#     db.session.delete(item)
#     db.session.commit()
    return render_template('delete.html', title='Delete item')

@app.route('/delete-list')
def delete_list():
    # itemList = ItemLists.query.get(id)
#     db.session.delete(itemList)
#     db.session.commit()
    return render_template('delete.html', title='Delete list')
