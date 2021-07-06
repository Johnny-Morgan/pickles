from django.shortcuts import render
from django.conf import settings
from .models import Product


def all_products(request):
    """ A view to show all products in the store,
    including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
        'discount_percentage': 100 - settings.DISCOUNT_PERCENTAGE,
    }

    return render(request, 'products/products.html', context)
