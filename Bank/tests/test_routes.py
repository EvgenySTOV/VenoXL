from flask import url_for
from flask_testing import TestCase
from Bank.app import app, db, Loan, User


# Create the base class
class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                          SECRET_KEY='123',
                          DEBUG=True,
                          WTF_CSRF_ENABLED=False
                          )
        return app

    # Will be called before every test
    def setUp(self):
        db.create_all()
        user = User(name="Rebecca", email="1@draft.com", password="12345678")
        loan = Loan(loan="500", payday="2022/12/04", author=user)

        db.session.add(user)
        db.session.add(loan)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('index'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        self.app.config['LOGIN_DISABLED'] = True
        response = self.client.get(url_for('new_loan_request'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        self.app.config['LOGIN_DISABLED'] = True
        response = self.client.get(url_for('update_request', loan_request_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        self.app.config['LOGIN_DISABLED'] = True
        response = self.client.get(url_for('delete_request', loan_request_id=1, follow_redirects=True))
        self.assertEqual(response.status_code, 302)
