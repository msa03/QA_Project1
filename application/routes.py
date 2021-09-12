from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Item, Manufacturer
from application.forms import itemForm, manForm


@app.route('/')
@app.route('/read', methods=['GET'])
def read():
    form = manForm()
    man = Manufacturer.query.all()
    return render_template('home.html', title="Home", man=man, form=form)

@app.route('/add-man', methods=['GET', 'POST'])
def add_man():
    form = manForm()
    if form.validate_on_submit():
        new_man = Manufacturer(
            manName = form.manName.data,
            manSpec = form.manSpec.data
            )
        db.session.add(new_man)
        db.session.commit()
        return redirect(url_for('add_item'))
    return render_template('add_man.html', title = "Add new manufacturer", form=form)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    form = itemForm()
    if form.validate_on_submit():
        new_item = Item(
            itemName = form.itemName.data,
            itemColour = form.itemColour.data,
            )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('add_item.html', title = "Add new item to manufacturer", form=form)

@app.route('/update-item', methods=['GET', 'POST'])
def update_item():
    form = itemForm()
    # item =Items.query.get(id)
#     if itemform.validate_on_submit():
#         item.name = itemform.name.data
#         db.session.commit()
#         redirect(url_for('home'))
#     elif request.method == 'GET':
#         itemform.name.data = item.name
    return render_template('update.html', title='Update item', form=form)

@app.route('/update-man/<int:manID>', methods=['GET', 'POST'])
def update_man(manID):
    form = manForm()
    man = Manufacturer.query.get(manID)
    if form.validate_on_submit():
        man.manName = form.manName.data
        man.manSpec = form.manSpec.data
        db.session.commit()
        redirect(url_for('read'))
    elif request.method == 'GET':
        form.manName.data = man.manName
        form.manSpec.data = man.manSpec
    return render_template('update_man.html', title='Update manufacturer name', form=form)

@app.route('/delete-item')
def delete_item():
    # item = Items.query.get(id)
#     db.session.delete(item)
#     db.session.commit()
    return redirect(url_for('read'))

@app.route('/delete-man/<int:manID>')
def delete_man(manID):
    man = Manufacturer.query.get(manID)
    db.session.delete(man)
    db.session.commit()
    return redirect(url_for('read', man=man))