from unittest import TestCase
from unittest.mock import patch
import blog.app as app
from blog.blog import Blog
from blog.post import Post


class AppTest(TestCase):

    #setup data for blog
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    # assert whether the menu prompt will be displayed
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    # assert menu calls
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('blog.app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', 'Test', 'q')
                app.menu()
                mocked_ask_read_blog.assert_called()

    def test_menu_calls_create_post(self):
        blog = app.blogs['Test']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Test', 'Post Title', 'Post Content', 'q')
            app.menu()
            self.assertEqual(blog.posts[0].title, 'Post Title')
            self.assertEqual(blog.posts[0].content, 'Post Content')

    # assert if available blogs can be displayed
    def test_print_blogs(self):
        blog = app.blogs['Test']
        blog.posts = ['Blog Test Content']
        app.blogs = {'Test': blog}
        # mocks a call for print
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            # assert whether it was called or not
            mocked_print.assert_called_with('- Test by Test Author (1 post)')

    # assert creating a blog
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    # assert reading/printing a blog
    def test_ask_read_blog(self):
        blog = app.blogs['Test']
        with patch('builtins.input', return_value='Test'):
            app.ask_read_blog()
            self.assertIsNotNone(app.blogs.get('Test'))
            with patch('blog.app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    # assert printing a post
    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {'Test': blog}
        with patch('blog.app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Post content')
        expected_print = '''
        --- Post Title ---
        
        Post content
        
        '''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    # assert creating a post
    def test_ask_create_post(self):
        blog = app.blogs['Test']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Post Title', 'Post Content')
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, 'Post Title')
            self.assertEquals(blog.posts[0].content, 'Post Content')
