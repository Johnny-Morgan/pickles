from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):

    def test_item_name_is_required(self):
        form = ProductForm({
            'name': '',
            'description': 'description',
            'price': 9.99,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_item_description_is_required(self):
        form = ProductForm({
            'name': 'name',
            'description': '',
            'price': 9.99,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors
                         ['description'][0], 'This field is required.')

    def test_item_price_is_required(self):
        form = ProductForm({
            'name': 'name',
            'description': 'description',
            'price': None,
            })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_item_price_is_6_digits_or_less(self):
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
