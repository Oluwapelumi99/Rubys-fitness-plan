from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Shop
from .cart import Cart

def cart_contents(request):

    cart_items = []
    total = 0
    shop_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'shop_count': shop_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

    # cart_items = []
    # total = 0
    # shop_count = 0
    # cart = request.session.get('cart', {})

    # for item_id, quantity in cart.items():
    #     shop = get_object_or_404(Shop, pk=item_id)
    #     total += quantity * shop.price
    #     shop_count += quantity
    #     cart_items.append({
    #         'item_id': item_id,
    #         'quantity': quantity,
    #         'shop': shop,
    #     })

    # delivery = 2.99
    
    # grand_total = delivery + total
    
    # context = {
    #     'cart_items': cart_items,
    #     'total': total,
    #     'shop_count': shop_count,
    #     'delivery': delivery,
    #     'grand_total': grand_total,
    # }

    # return context

def cart(request):
    return{'cart': Cart(request)}