from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.conf import settings
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ View that renders the shopping basket contents page """

    context = {
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        }
    return render(request, 'basket/basket.html', context)


def add_product_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'{product.name} quantity updated to \
            {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} added to basket')

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    basket[item_id] = quantity
    messages.success(request, f'{product.name} quantity updated to \
            {basket[item_id]}')
    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'{product.name} removed from basket')
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
