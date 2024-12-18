from django.shortcuts import render, redirect, reverse, get_object_or_404
from exercises.models import Exercise

# Create your views here.

def view_cart(request):
    """ A view to return the cart items page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    # print(request.session['bag'])
    return redirect(redirect_url)
    