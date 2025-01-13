from urllib.parse import urlencode
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.messages import get_messages
from .models import Blog
import tempfile
from .forms import CommentForm


class TestViews(TestCase):
    '''
    Unit tests for the blog app views
    '''

    def setUp(self):
        '''
        set up a staff user and log them in
        to test the blog crud functionality
        '''
        email = 'test@test.com'
        password = 'testpassword1234'
        first_name = 'testFirst'
        last_name = 'testLast'
        user_model = get_user_model()
        self.user = user_model.objects.create_staffuser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name)
        log_in = self.client.login(email=email, password=password)

        # confirm user is logged in
        self.assertTrue(log_in)
        self.assertTrue(self.user.is_staff)
        # create a comment for the test db
        title = 'test title'
        blog = Blog.objects.create(name='testCategory')
        content = 'testContent'
        self.blog = Blog.objects.create(
            title=title,
            author=self.user, content=content)
        posts = BlogPost.objects.all()

    def test_blog_page(self):
        '''
        test the blog page url
        '''
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_page_template(self):
        '''
        test the correct template is used for the blog page
        '''
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, template_name='blog/blog.html')

    def test_posts_passed_into_template(self):
        '''
        test that the blog posts are passed into the blog template
        '''
        response = self.client.get('/blog/')
        posts = BlogPost.objects.all()
        self.assertEqual(len(response.context['posts']), len(posts))

    def test_blog_post_detail_page(self):
        '''
        test the blog post detail page
        create a blog post then check the page
        '''
        posts = BlogPost.objects.all()
        post = posts[0]
        response = self.client.get(f'/blog/{post.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_template(self):
        '''
        test the correct template is used for the blog post detail page
        '''
        posts = BlogPost.objects.all()
        post = posts[0]
        response = self.client.get(f'/blog/{post.slug}/')
        self.assertTemplateUsed(
            response,
            template_name='blog/blog_post_detail.html')

    def test_add_blog_post_page(self):
        '''
        test to see if staff user logged in can access add blog post page
        '''
        response = self.client.get('/blog/add-post/')
        self.assertEqual(response.status_code, 200)

    def test_add_blog_post_page_template(self):
        '''
        test the correct template is used for the add blog post page
        '''
        response = self.client.get('/blog/add-post/')
        self.assertTemplateUsed(
            response,
            template_name='blog/blog_post_form.html')

    def test_logged_out_user_redirected_from_add_blog_post_page(self):
        '''
        test to ensure logged out user is redirected
        and can not access add blog post page
        '''
        self.client.logout()
        response = self.client.get('/blog/add-post/')
        self.assertEqual(response.status_code, 302)

    def test_adding_blog_post(self):
        '''
        test to check that logged in staff user
        can add a blog post through the page
        -checks the current number of blogposts
        -encodes the data for the new blog post
        -posts the data to the url
        -receives the messages that are returned,
        -confirms the message contains the success tag
        -confirms the redirect
        -confirms that the number of blogposts has increased by one
        '''
        self.assertEqual(BlogPost.objects.count(), 1)
        data = urlencode({
            'title': 'page submitted blog post',
            'category': '1',
            'image_url': 'https://en.wikipedia.org/wiki/File:Test_image.jpg',
            'image': None,
            'content': 'page submitted blog post content'})
        response = self.client.post(
            '/blog/add-post/',
            data,
            content_type='application/x-www-form-urlencoded')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 2)

    def test_editing_blog_post(self):
        '''
        test to ensure that edits made to a blog post
        are recorded correctly
        '''
        post = BlogPost.objects.get(title='test title')
        slug = post.slug
        response = self.client.post(reverse('edit_blog_post',
                                    kwargs={'slug': slug}),
                                    {
                                    'title': 'test edited title',
                                    'category': '1',
                                    'content': 'test content'})
        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertEqual(post.title, 'test edited title')

    def test_delete_blog_post(self):
        '''
        test delete blog post view
        '''
        post = BlogPost.objects.get(title='test title')
        self.assertEqual(BlogPost.objects.count(), 1)
        response = self.client.post(reverse(
            'delete_blog_post', kwargs={'pk': post.id}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_logged_out_user_delete_blog_post(self):
        '''
        test if the user is logged out
        that they can't delete a blog post
        by sending the request to the url
        '''
        post = BlogPost.objects.get(title='test title')
        self.assertEqual(BlogPost.objects.count(), 1)
        self.client.logout()
        response = self.client.get(reverse(
            'delete_blog_post', kwargs={'pk': post.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 1)