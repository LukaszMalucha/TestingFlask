import unittest
from models.store import StoreModel
from base_test import BaseTest



class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        
        self.assertEqual(store.name, 'test')
        
        




if __name__ == '__main__':
    unittest.main()                              
        