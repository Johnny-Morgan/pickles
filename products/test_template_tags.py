from django.test import TestCase
from .templatetags.products_tools import calc_discounted_price


class TestCategoryModel(TestCase):

    def test_calc_discounted_price_works(self):
        self.assertEqual(calc_discounted_price(100, 10), 90)
        self.assertEqual(calc_discounted_price(100, 20), 80)
        self.assertEqual(calc_discounted_price(200, 50), 100)
