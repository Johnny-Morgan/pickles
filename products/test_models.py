from django.test import TestCase
from .models import Category


class TestCategoryModel(TestCase):
    def create_category(self, name='name', friendly_name='friendly_name'):
        return Category.objects.create(name=name, friendly_name=friendly_name)

    def test_category_creation(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))

    def test_category_string_method_returns_name(self):
        category = Category.objects.create(name='name',
                                           friendly_name='friendly_name')
        self.assertEqual(str(category), 'name')

