from django.shortcuts import render, redirect
from django.conf import settings


def view_basket(request):
    """ View that renders the shopping basket contents page """
    context = {
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        }
    return render(request, 'basket/basket.html', context)


def add_product_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)
