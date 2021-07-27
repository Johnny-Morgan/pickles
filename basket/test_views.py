from django.test import TestCase
from .templatetags.basket_tools import calc_subtotal


class TestBasketViews(TestCase):

    def test_get_view_basket_page(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_calc_subtotal_works(self):
        self.assertEqual(calc_subtotal(5.75, 10), 57.50)
        self.assertEqual(calc_subtotal(20, 2), 40)
        self.assertEqual(calc_subtotal(17.95, 10), 179.50)
