from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):

    def test_item_title_is_required(self):
        form = PostForm({
            'title': '',
            'intro': 'intro',
            'body': 'abcdefghijklmno',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_item_intro_is_required(self):
        form = PostForm({
            'title': 'title',
            'intro': '',
            'body': 'abcdefghijklmno',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('intro', form.errors.keys())
        self.assertEqual(form.errors['intro'][0], 'This field is required.')

    def test_item_body_is_required(self):
        form = PostForm({
            'title': 'title',
            'intro': 'intro',
            'body': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_item_body_is_at_least_15_characters(self):
        form = PostForm({
            'title': 'title',
            'intro': 'intro',
            'body': 'body',
            })
        self.assertFalse(form.is_valid())

    def test_tags_field_is_not_required(self):
        form = PostForm({
            'title': 'title',
            'intro': 'intro',
            'body': 'abcdefghijklmno',
            })
        self.assertTrue(form.is_valid())

    def test_excludes_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(form.Meta.exclude, ['slug'])
