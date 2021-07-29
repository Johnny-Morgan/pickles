from django.test import TestCase
from .models import Category, Product, Review


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

    def test_category_get_friendly_name_method_returns_friendly_name(self):
        category = Category.objects.create(name='name',
                                           friendly_name='friendly_name')
        self.assertEqual(Category.get_friendly_name(category), 'friendly_name')


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
        product = Product()
        self.assertTrue(isinstance(product, Product))

    def test_product_string_method_returns_name(self):
        category = Category.objects.create(name='name',
                                           friendly_name='friendly_name')
        product = Product.objects.create(category=category, sku='sku',
                                         name='name', description='desc',
                                         price=10, on_sale=True,
                                         image_url='url', image='image')
        self.assertEqual(str(product), 'name')


class TestReviewModel(TestCase):

    def test_review_string_method(self):
        product = Product(name='Blueberry Bush')
        review = Review(product=product, name='Jimmy McNulty')
        expected_result = 'Blueberry Bush review by Jimmy McNulty'
        self.assertEqual(str(review), expected_result)
