from django.test import TestCase
from .models import Post, Tag, Comment


class TestTagModel(TestCase):

    def create_tag(self, title='title',):
        return Tag.objects.create(title=title)

    def test_tag_creation(self):
        tag = self.create_tag()
        self.assertTrue(isinstance(tag, Tag))

    def test_tag_string_method_returns_title(self):
        tag = Tag.objects.create(title='Test Blog Tag')
        self.assertEqual(str(tag), 'Test Blog Tag')


class TestPostModel(TestCase):
    def create_post(self, title='title',
                    intro='intro',
                    body='abcdefghijklmno'):
        return Post.objects.create(title=title, intro=intro, body=body)

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))

    def test_post_string_method_returns_title(self):
        post = Post.objects.create(title='Title',
                                   intro='intro',
                                   body='abcdefghijklmno')
        self.assertEqual(str(post), 'Title')


class TestCommentModel(TestCase):

    def test_comment_string_method_returns_name(self):
        post = Post.objects.create(title='Title',
                                   intro='intro',
                                   body='abcdefghijklmno')
        comment = Comment.objects.create(post=post,
                                         name='name',
                                         email='email',
                                         body='body')
        self.assertEqual(str(comment), 'name')
