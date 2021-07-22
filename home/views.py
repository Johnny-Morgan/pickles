from django.shortcuts import render
from products.models import Product


def index(request):
    """View to render the home page"""
    sale_items_set_1 = Product.objects.filter(on_sale=True)[:3]
    sale_items_set_2 = Product.objects.filter(on_sale=True)[3:6]
    context = {
        'sale_items_set_1': sale_items_set_1,
        'sale_items_set_2': sale_items_set_2,
    }
    return render(request, 'home/index.html', context)


def error_404(request, exception):
    """View to render a cutom 404 page"""
    return render(request, '../templates/404.html')
