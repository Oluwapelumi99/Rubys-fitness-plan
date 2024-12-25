from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QNmQ6J0bThu4857mrjTo8hYSTPLOjfx03yU5TbnW2RIo5mJrsyyYsIfb9uOXHmePiGB69mWcCLzJsHBG1gPCPUd00OaIBgNZS',
        'client_secret': 'intent.client_secret',
    }

    return render(request, template, context)