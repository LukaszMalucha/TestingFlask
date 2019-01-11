import unittest
from models.item import ItemModel
from base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            
            self.assertIsNone(ItemModel.find_by_name('test'))
            
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            

if __name__ == '__main__':
    unittest.main()                      