import unittest
from Bank.app import app


class TestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        tester = app.test_client(self)
        response = tester.get('/profile', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_all(self):
        tester = app.test_client(self)
        response = tester.get('/all', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_new(self):
        tester = app.test_client(self)
        response = tester.get('/new', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_update(self):
        tester = app.test_client(self)
        response = tester.get('/request/1/update', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_delete(self):
        tester = app.test_client(self)
        response = tester.get('request/1/delete', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
