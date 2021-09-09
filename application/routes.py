from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Items, ItemLists, ItemListLinks
from application.forms import ItemForm, ItemListForm, ItemLinkForm


@app.route('/', methods=['GET', 'POST'])
def home():
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
    return render_template('home.html', title="Homepage", form=form)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    itemform = ItemForm()
#     # if itemform.validate_on_submit():
#     #     item = Items(
#     #         name = itemform.name.data,
#     #         quantity = itemform.quantity.data,
#     #         age_restriction = itemform.age_restriction.data
#     #     )
#     #     db.session.add(item)
#     #     db.session.commit()
#     #     return redirect(url_for('home'))
    return render_template('add_item.html', title = "Add new item to list", form=itemform)

@app.route('/add_list', methods=['GET', 'POST'])
def add_list():
    itemlistform = ItemListForm()
#     if itemlistform.validate_on_submit():
#         itemList = ItemLists(
#             list_name = itemlistform.list_name.data
#         )
#         db.session.add(itemList)
#         db.session.commit()
#         return redirect(url_for('home'))
    return render_template('add_list.html', title = "Create new list", form=itemlistform)

@app.route('/update_item', methods=['GET', 'POST'])
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

@app.route('/update_list', methods=['GET', 'POST'])
def update_list():
    itemlistform = ItemListForm()
    # itemList =ItemLists.query.get(id)
#     if itemlistform.validate_on_submit():
#         itemList.name = itemlistform.name.data
#         db.session.commit()
#         redirect(url_for('home'))
#     elif request.method == 'GET':
#         itemlistform.name.data = itemList.name
    return render_template('update.html', title='Update shopping list name', form=itemlistform)

@app.route('/delete')
def delete_item():
    # item = Items.query.get(id)
#     db.session.delete(item)
#     db.session.commit()
    return render_template('delete.html')

@app.route('/delete')
def delete_list():
    # itemList = ItemLists.query.get(id)
#     db.session.delete(itemList)
#     db.session.commit()
    return render_template('delete.html')
