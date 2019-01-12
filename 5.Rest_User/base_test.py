"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""
import unittest
from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    ## once per test case(whole test class)
    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
        
    ## once per each test(method)
    def setUp(self):
        # Make sure database exists
        with app.app_context():        
            db.create_all()
        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()                      