from django.shortcuts import render
from products.models import Product


def index(request):
    """View to render the home page"""
    sale_items = Product.objects.filter(on_sale=True)
    sale_items_set_1 = sale_items[:3]
    sale_items_set_2 = sale_items[3:6]
    context = {
        'sale_items': sale_items,
        'sale_items_set_1': sale_items_set_1,
        'sale_items_set_2': sale_items_set_2,
    }
    return render(request, 'home/index.html', context)


def error_403(request, exception):
    """View to render a cutom 403 page"""
    return render(request, '../templates/403.html')


def error_404(request, exception):
    """View to render a cutom 404 page"""
    return render(request, '../templates/404.html')


def error_500(request):
    """View to render a cutom 500 page"""
    return render(request, '../templates/500.html')
