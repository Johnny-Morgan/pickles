from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

from .models import Post


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpass')

    def test_get_blog_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_get_post_page(self):
        post = Post.objects.create(title='title', slug='title',
                                   intro='intro', body='abcdefghijklmno')
        response = self.client.get(f'/blog/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')

    def test_get_edit_post_page(self):
        self.client.login(username='admin', password='adminpass')
        post = Post.objects.create(title='title', slug='title',
                                   intro='intro', body='abcdefghijklmno')
        response = self.client.get(f'/blog/edit/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')

    def test_can_edit_post(self):
        self.client.login(username='admin', password='adminpass')
        post = Post.objects.create(title='title', slug='title',
                                   intro='intro', body='abcdefghijklmno')
        response = self.client.post(f'/blog/edit/{post.slug}/', {
                                    'title': 'title',
                                    'intro': 'Updated intro',
                                    'body': 'abcdefghijklmno'
                                    })
        self.assertRedirects(response, f'/blog/{post.slug}/')
        updated_post = Post.objects.get(id=post.id)
        self.assertEqual(updated_post.intro, 'Updated intro')

    def test_can_add_post(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/blog/add/',
                                    {'title': 'title', 'intro': 'intro',
                                     'body': 'abcdefghijklmno'})
        self.assertRedirects(response, '/blog/')

    def test_can_delete_post(self):
        self.client.login(username='admin', password='adminpass')
        post = Post.objects.create(title='title', slug='title',
                                   intro='intro', body='abcdefghijklmno')
        response = self.client.get(f'/blog/delete_post/{post.id}/')
        self.assertRedirects(response, '/blog/')
        existing_items = Post.objects.filter(id=post.id)
        self.assertEqual(len(existing_items), 0)
