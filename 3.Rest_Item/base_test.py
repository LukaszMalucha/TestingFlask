from unittest import TestCase
from app import app
from db import db



class BaseTest(TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'        ## blank sqlite file for testing
        
        ## Load app variables
        with app.app_context():
            db.init_app(app)
            db.create_all()
        
        # app.testing  = True
        self.app  = app.test_client
        self.app_context = app.app_context
        
        
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
            
if __name__ == '__main__':
    unittest.main()                      