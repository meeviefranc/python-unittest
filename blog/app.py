from blog.blog import Blog

# blog_name : blog object
blogs = dict()

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post or "q" to quit : '
POST_TEMPLATE = '''
        --- {} ---
        
        {}
        
        '''


def print_blogs():
    # print the available blogs
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    # ask user for new title, name and create a new blog under their name
    title = input('Enter title: ')
    author = input('Enter author: ')
    blogs[title] = Blog(title, author)


def ask_create_post():
    # ask for a blog title, post title and post content as new post in the blog specified
    blog_title = input('Enter blog title to post content: ')
    post_title = input('Enter post content title: ')
    post_content = input('Enter post content: ')
    blogs[blog_title].create_post(post_title, post_content)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def ask_read_blog():
    # ask for a blog title and prints a post
    title = input('Enter title: ')
    print_posts(blogs[title])


def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)
