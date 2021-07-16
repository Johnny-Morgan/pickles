from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J2D6JHtzlyhlPp0SVwXYlFd7G80SpQQmj11kS33EZShM3UksHMU1ZgVZ0RldGWMWV3PMePgQlclD1WFrSB5vJYA00JrRjQ1NG',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
