from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from shop.models import Shop



# Create your views here.

def view_cart(request):
    """ A view to return the cart items page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add quantity ans sizes to the cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'shop_size' in request.POST:
        size = request.POST['shop_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    """Update the quantity of the cart and update the price accordingly"""

    shop = get_object_or_404(Shop, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'shop_size' in request.POST:
        size = request.POST['shop_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size} {shop.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size} {shop.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {shop.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {shop.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

    