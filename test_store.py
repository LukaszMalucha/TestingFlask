import unittest
from models.store import StoreModel
from base_test import BaseTest



class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        
        self.assertEqual(store.name, 'test')
        
    def test_create_duplicate_store(self):
        

        
    def test_delete_store(self):
        
    def test_find_store(self):
    
    def test_store_not_found(self):

    def test_store_found_with_items(self):
        
    def test_store_list(self):
        
    def test_store_list_with_items(self):    

if __name__ == '__main__':
    unittest.main()                              
        