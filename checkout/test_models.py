from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product, Category


class TestOrderModel(TestCase):

    def create_order(self):
        return Order.objects.create()

    def test_order_creation(self):
        order = self.create_order()
        self.assertTrue(isinstance(order, Order))

    def test_order_string_method_returns_title(self):
        order = Order.objects.create(order_number='12345678')
        self.assertEqual(str(order), '12345678')


class TestOrderLineItemModel(TestCase):

    def create_order_line_item(self):
        category = Category.objects.create(name='name',
                                           friendly_name='friendly_name')

        product = Product.objects.create(category=category, sku='sku_num',
                                         name='name', description='desc',
                                         price=10, on_sale=True,
                                         image_url='url', image='image')
        order = Order.objects.create(order_number='12345678')

        return OrderLineItem.objects.create(order=order, product=product,
                                            quantity=1, lineitem_total=10)

    def test_order_line_item_creation(self):
        order_line_item = self.create_order_line_item()
        self.assertTrue(isinstance(order_line_item, OrderLineItem))

    def test_order_line_item_string_method(self):
        order_line_item = self.create_order_line_item()

        self.assertEqual(str(order_line_item), 'SKU sku_num on order 12345678')
