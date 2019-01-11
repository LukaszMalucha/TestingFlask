from base_test import BaseTest
import json




class TestHome(unittest.TestCase):
    def test_home(self):
        with self.app as c:                                     ## initialize test context
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)             ## status code
            self.assertEqual(json.loads(resp.get_data()),       ## compare response 
                            {'message': 'Hello, world!'}
                            )
            


## py.test

if __name__ == '__main__':
    unittest.main()                 