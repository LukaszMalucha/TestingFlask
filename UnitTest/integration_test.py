import unittest
from blog_class.blog import Blog
from post_class.post import Post

class BlogTest(unittest.TestCase):
    
        
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        
        
    def test_json(self):
        b = Blog('Test', 'Test Author')      
        b.create_post('Test Post', 'Test Content')
        
        expected = {'title': 'Test', 
                    'author': 'Test Author', 
                    'posts': [
                        {'title': 'Test Post',
                        'content': 'Test Content'}
                          ]
                    }
                    
        self.assertDictEqual(expected, b.json())
        
if __name__ == '__main__':
    unittest.main()