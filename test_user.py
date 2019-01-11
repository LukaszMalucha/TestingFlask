import unittest
from models.user import UserModel
from base_test import BaseTest



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
            

if __name__ == '__main__':
    unittest.main()                 