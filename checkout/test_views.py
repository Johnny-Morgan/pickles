from django.test import TestCase, Client
from django.urls import reverse


class TestCheckoutViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout = reverse('checkout')

    def test_checkout_view(self):
        """ Redirect to products page with empty basket"""
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
