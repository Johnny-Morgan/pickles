from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):
    def create_post(self, title='title',
                    intro='intro',
                    body='abcdefghijklmno'):
        return Post.objects.create(title=title, intro=intro, body=body)

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
