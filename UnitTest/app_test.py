import unittest
from unittest.mock import patch
from blog_class.blog import Blog
import app





class AppTest(unittest.TestCase):
    
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}        

            
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
        
            
    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):                           ### addditionally simulate input
                app.menu()
                mocked_print_blogs.assert_called()
                
    def test_print_blogs(self):
        ### CONTEXT with fake print call
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')
            
            
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')          ## returns for the first time & second time function is called (as two inputs are needed)
            app.ask_create_blog()
            
            self.assertIsNotNone(app.blogs.get('Test'))
            
            
    def test_ask_read_blog(self):
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                
                mocked_print_post.assert_called_with(app.blogs['Test'])
        
    def test_print_posts(self):
    blog = app.blogs['Test']
        
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            
            mocked_print_post.assert_called_with(blog.posts[0])
        
            
if __name__ == '__main__':
    unittest.main()            