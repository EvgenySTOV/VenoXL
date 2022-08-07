import unittest
import flask_testing as flaskr
from flask import url_for
from flask_login import login_required
from flask_testing import TestCase
from .app import app, db, User, Loan


# Create the base class
class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                          SECRET_KEY='TEST_SECRET_KEY',
                          DEBUG=True,
                          WTF_CSRF_ENABLED=False
                          )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test team
        loan1 = Loan(loan="6000")

        # save users to database
        db.session.add(loan1)

    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()


# Write a test class to test login authorization
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('user_loan_request'))
        self.assertEqual(response.status_code, 401)
