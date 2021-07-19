from django.test import TestCase
from .forms import ProductForm, ReviewForm


class TestProductForm(TestCase):

    def test_product_name_is_required(self):
        form = ProductForm({
            'name': '',
            'description': 'description',
            'price': 9.99,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_description_is_required(self):
        form = ProductForm({
            'name': 'name',
            'description': '',
            'price': 9.99,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors
                         ['description'][0], 'This field is required.')

    def test_product_price_is_required(self):
        form = ProductForm({
            'name': 'name',
            'description': 'description',
            'price': None,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_price_is_6_digits_or_less(self):
        form = ProductForm({
            'name': 'name',
            'description': 'description',
            'price': 1234567,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
                    form.errors['price'][0],
                    'Ensure that there are no more than 6 digits in total.')

    def test_product_price_has_no_more_than_4_digits_before_decimal(self):
        form = ProductForm({
            'name': 'name',
            'description': 'description',
            'price': 12345.00,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
                    form.errors['price'][0],
                    'Ensure that there are no more than 4 digits before the decimal point.')

    def test_sku_field_is_not_required(self):
        form = ProductForm({
            'name': 'name',
            'description': 'description',
            'price': 9.99,
            })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')


class TesReviewForm(TestCase):

    def test_review_name_is_required(self):
        form = ReviewForm({
            'name': '',
            'email': 'email@email.com',
            'review': 'review',
            'rating': '1',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_review_email_is_required(self):
        form = ReviewForm({
            'name': 'name',
            'email': '',
            'review': 'review',
            'rating': '1',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_review_review_is_required(self):
        form = ReviewForm({
            'name': 'name',
            'email': 'email@email.com',
            'review': '',
            'rating': '1',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('review', form.errors.keys())
        self.assertEqual(form.errors['review'][0], 'This field is required.')

    def test_review_rating_is_required(self):
        form = ReviewForm({
            'name': 'name',
            'email': 'email@email.com',
            'review': '',
            'rating': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_review_email_is_valid(self):
        form = ReviewForm({
            'name': 'name',
            'email': 'email',
            'review': 'review',
            'rating': '1'
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'Enter a valid email address.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields,
                         ['name', 'email', 'review', 'rating'])
