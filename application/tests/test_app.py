from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Manufacturer, Item

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        sampleMan = Manufacturer(manName="TestMan", manSpec="TestSpec")
        db.session.add(sampleMan)
        db.session.commit()

        sampleItem = Item(itemName="TestName", itemColour="TestColour")
        db.session.add(sampleItem)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

