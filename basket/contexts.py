from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)

        if product.on_sale:
            price = round(product.price * Decimal(1 -
                          settings.DISCOUNT_PERCENTAGE / 100), 2)
        else:
            price = product.price

        total += quantity * price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'price': price
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    if product_count == 0:
        delivery = 0

    order_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'order_total': order_total,
        'delivery_charge': settings.DELIVERY_COST,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
    }

    return context
