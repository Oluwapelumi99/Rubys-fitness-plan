from django.shortcuts import render, redirect, reverse, get_object_or_404
from .cart import Cart
from shop.models import Shop
from django.http import JsonResponse


# Create your views here.

def view_cart(request):
    """ A view to return the cart items page """

    carts = Cart(request)
    cart_items = carts.get_items

    return render(request, 'cart/cart.html', {'cart_items': cart_items})


def add_to_cart(request):
    """ Add a quantity of the specified product to the shopping bag """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        shop_id = int(request.POST.get('shop_id'))
        shop = get_object_or_404(Shop, id=shop_id)
        cart.add(shop=shop)
        # response = JsonResponse({'Shop Name: ': shop.name})
        cart_quantity = cart.__len__()
        response = JsonResponse({'cart_quantity': cart_quantity})
        return response



# def add_to_cart(request, item_id):
#     """ Add a quantity of the specified product to the shopping bag """

#     quantity = int(request.POST.get('quantity'))
#     redirect_url = request.POST.get('redirect_url')
#     cart = request.session.get('cart', {})

#     if item_id in list(cart.keys()):
#         cart[item_id] += quantity
#     else:
#         cart[item_id] = quantity

#     request.session['cart'] = cart
#     print(request.session['cart'])
#     return redirect(redirect_url)
    