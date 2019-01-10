import unittest
from post_class.post import Post



class PostTest(unittest.TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)
        
    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
        
        self.assertDictEqual(expected, p.json())
        
if __name__ == '__main__':
    unittest.main()