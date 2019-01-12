import unittest
from models.user import UserModel
from base_test import BaseTest
import json



class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')
        
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.password, 'abcd')
        
        
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')
            
            self.assertIsNone(UserModel.find_by_username('test'))
            self.assertIsNone(UserModel.find_by_id(1))
            
            user.save_to_db()
            
            self.assertIsNotNone(UserModel.find_by_username('test'))
            self.assertIsNotNone(UserModel.find_by_id(1))
            
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'test', 'password': '1234'})
                
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                       json.loads(response.data)) ## convert to python dictionary
        
    def test_user_login(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_response = client.post('/auth', 
                                            data=json.dumps({'username': 'test','password': '1234'}),
                                            headers={'Content-Type': 'application/json'})
                
                self.assertIn('access_token', json.loads(auth_response.data).keys())
    
    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'}) 
                response = client.post('/register', data={'username': 'test', 'password': '1234'})
                
                self.assertEqual(response.status_code, 400)







if __name__ == '__main__':
    unittest.main()                 