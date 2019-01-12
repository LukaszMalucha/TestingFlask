import unittest
from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        ## call original BaseTest setup
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth', data=json.dumps({'username':'test', 'password': '1234'}),
                                                    headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = 'JWT' + auth_token
        
    
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()    ## for foreign key testing (mysql, postgres)
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))


    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            self.assertEqual(item.store.name, 'test_store')
            
    
    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test')
                self.assertEqual(resp.status_code, 401)
        
        
        
    def test_get_item_not_found(self):    
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test', headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 404)
        
    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                resp = client.get('/item/test', headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 200)
        
    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                resp = client.delete('/item/test')
                self.assertEqual(resp.status_code, 200)
              
    
    def test_create_item(self):    
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                
                resp = client.post('/item/test', data={'price': 17.99, 'store_id': 1})
                
                self.assertEqual(resp.status_code, 201)


    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()        
                ItemModel('test', 19.99, 1).save_to_db()
                
                resp = client.post('/item/test', data={'price': 17.99, 'store_id': 1})
                
                self.assertEqual(resp.status_code, 400)
        


if __name__ == '__main__':
    unittest.main()                      