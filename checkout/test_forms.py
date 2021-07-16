from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_first_name_is_required(self):
        form = OrderForm({
            'first_name': '',
            'last_name': 'last_name',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')

    def test_last_name_is_required(self):
        form = OrderForm({
            'last_name': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({
            'email': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_mobile_number_is_required(self):
        form = OrderForm({
            'mobile_number': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('mobile_number', form.errors.keys())
        self.assertEqual(form.errors['mobile_number'][0],
                         'This field is required.')

    def test_street_address1_is_required(self):
        form = OrderForm({
            'street_address1': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_town_or_city_is_required(self):
        form = OrderForm({
            'town_or_city': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_country_is_required(self):
        form = OrderForm({
            'country': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0],
                         'This field is required.')

    def test_email_is_valid(self):
        form = OrderForm({
            'email': 'email'
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'Enter a valid email address.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
                         'first_name', 'last_name', 'email',
                         'mobile_number', 'street_address1', 'street_address2',
                         'town_or_city', 'county', 'postcode', 'country',
                         ))
