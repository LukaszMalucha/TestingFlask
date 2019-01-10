import unittest
from blog_class.blog import Blog

class BlogTest(unittest.TestCase):
    
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        
        
        self.assertEqual('Test', b.title)    
        self.assertEqual('Test Author', b.author) 
        self.assertListEqual([], b.posts) 
        self.assertEqual(0, len(b.posts)) 
        
        
    def test_repr(self):
        b = Blog('Test', 'Test Author')
        
        self.assertEqual(b.__repr__(), '{} by {} (0 posts)'.format(b.title,b.author))
        
        
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')

        
        
if __name__ == '__main__':
    unittest.main()