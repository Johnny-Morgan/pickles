from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):

    def test_blog_title_is_required(self):
        form = PostForm({
            'title': '',
            'intro': 'intro',
            'body': 'abcdefghijklmno',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_blog_intro_is_required(self):
        form = PostForm({
            'title': 'title',
            'intro': '',
            'body': 'abcdefghijklmno',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('intro', form.errors.keys())
        self.assertEqual(form.errors['intro'][0], 'This field is required.')

    def test_blog_body_is_required(self):
        form = PostForm({
            'title': 'title',
            'intro': 'intro',
            'body': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_blog_body_is_at_least_15_characters(self):
        form = PostForm({
            'title': 'title',
            'intro': 'intro',
            'body': 'body',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'Ensure this value has at least 15 characters (it has 4).')

    def test_tags_field_is_not_required(self):
        form = PostForm({
            'title': 'title',
            'intro': 'intro',
            'body': 'abcdefghijklmno',
            })
        self.assertTrue(form.is_valid())

    def test_excludes_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(form.Meta.exclude, ['slug', 'author'])


class TestCommentForm(TestCase):

    def test_comment_name_is_required(self):
        form = CommentForm({
            'name': '',
            'email': 'email@email.com',
            'body': 'body',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_comment_email_is_required(self):
        form = CommentForm({
            'name': 'name',
            'email': '',
            'body': 'body',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_comment_body_is_required(self):
        form = CommentForm({
            'name': 'name',
            'email': 'email@email.com',
            'body': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_comment_email_is_valid(self):
        form = CommentForm({
            'name': 'name',
            'email': 'email',
            'body': 'body',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'Enter a valid email address.')

    def test_excludes_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.exclude, ['post'])
