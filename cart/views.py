from shop.models import Shop
from django.contrib import messages
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)


# Create your views here.

def view_cart(request):
    """ A view to return the cart items page:model:`Shop`

    **Context**

    ``shop``
    using the :model:`Shop` from the shop app.

    **Template:**

    :template: 'cart/cart.html'`
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity and sizes to the cart:model:`Shop`

    **Context**

    ``shop``
    using the :model:`Shop` from the shop app.

    """
    shop = get_object_or_404(Shop, pk=item_id)
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
                messages.success(
                    request, (
                        f'Updated size {size} {shop.name} quantity'
                        'to {cart[item_id]["items_by_size"][size]}'))
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size} {shop.name} to your bag')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size} {shop.name} to your bag')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {shop.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {shop.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of the cart and update the price
    accordingly:model:`Shop`

    **Context**

    ``shop``
    using the :model:`Shop` from the shop app.
    """

    shop = get_object_or_404(Shop, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'shop_size' in request.POST:
        size = request.POST['shop_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, (
                    f'Updated size {size} {shop.name} quantity '
                    'to{cart[item_id]["items_by_size"][size]}'))
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed size {size} {shop.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                    request,
                    f'Updated {shop.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {shop.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_item(request, item_id):
    """Remove the item from the cart:model:`Shop`

    **Context**

    ``shop``
    using the :model:`Shop` from the shop app.
    """

    try:
        shop = get_object_or_404(Shop, pk=item_id)
        size = None

        if 'shop_size' in request.POST:
            size = request.POST['shop_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed size {size} {shop.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {shop.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
