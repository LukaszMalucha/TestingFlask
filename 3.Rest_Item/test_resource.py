import unittest
from models.item import ItemModel


class ItemTest(unittest.TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)
        
        self.assertEqual(item.name, 'test', "The name doesn't match")
        self.assertEqual(item.price, 19.99, "The price doesn't match")
    
    def test_item_json(self):
        item = ItemModel('test', 19.99)
        expected = {
            'name': 'test',
            'price': 19.99,
        }

        self.assertEqual(item.json(), expected, "JSON not correct")

## py.test

if __name__ == '__main__':
    unittest.main()                 