from django.shortcuts import render, get_object_or_404
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


def product_info(request, product_id):
    """ A view to show individual product information """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)