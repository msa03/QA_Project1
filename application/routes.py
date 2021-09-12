from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Lists, Items
from application.forms import ListForm, ItemForm


@app.route('/')
@app.route('/read', methods=['GET'])
def read():
    form = ListForm()
    lists = Lists.query.all()
    return render_template('home.html', lists=lists, form=form)

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

@app.route('/update-list/<int:id>', methods=['GET', 'POST'])
def update_list(id):
    form = ListForm()
    lists = Lists.query.get(id)
    if form.validate_on_submit():
        lists.list_name = form.list_name.data
        db.session.commit()
        redirect(url_for('read'))
    elif request.method == 'GET':
        form.list_name.data = lists.list_name
    return render_template('update.html', title='Update list name', form=form)

@app.route('/delete-item')
def delete_item():
    # item = Items.query.get(id)
#     db.session.delete(item)
#     db.session.commit()
    return redirect(url_for('read'))

@app.route('/delete-list/<int:id>')
def delete_list(id):
    lists = Lists.query.get(id)
    db.session.delete(lists)
    db.session.commit()
    return redirect(url_for('read', lists=lists))