from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Manufacturer, Item

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        sampleMan = Manufacturer(manName="TestMan", manSpec="TestSpec")
        db.session.add(sampleMan)
        db.session.commit()

        sampleItem = Item(itemName="TestName", itemColour="TestColour")
        db.session.add(sampleItem)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

