from django.test import TestCase
from .models import Category, Product


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


class TestProductModel(TestCase):

    category = Category.objects.create(name='name',
                                       friendly_name='friendly_name')

    def create_product(self, category=category, sku='sku',
                       name='name', description='desc',
                       price=10, on_sale=True,
                       image_url='url', image='image'):
        return Product.objects.create(category=category, sku=sku, name=name,
                                      description=description, price=price,
                                      on_sale=on_sale, image_url=image_url,
                                      image=image)

    def test_product_creation(self):
        product = self.create_product()
        self.assertTrue(isinstance(product, Product))

    def test_product_string_method_returns_name(self):
        category = Category.objects.create(name='name',
                                           friendly_name='friendly_name')
        product = Product.objects.create(category=category, sku='sku',
                                         name='name', description='desc',
                                         price=10, on_sale=True,
                                         image_url='url', image='image')
        self.assertEqual(str(product), 'name')
