from django.test import TestCase
from .models import Post, Tag


class TestPostModel(TestCase):
    def create_post(self, title='title',
                    intro='intro',
                    body='abcdefghijklmno'):
        return Post.objects.create(title=title, intro=intro, body=body)

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))

    def test_tag_string_method_returns_title(self):
        tag = Tag.objects.create(title='Test Blog Tag')
        self.assertEqual(str(tag), 'Test Blog Tag')

    def test_post_string_method_returns_title(self):
        post = Post.objects.create(title='Title',
                                   intro='intro',
                                   body='abcdefghijklmno')
        self.assertEqual(str(post), 'Title')
