from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Shop
from .cart import Cart

# def cart_contents(request):

#     cart_items = []
#     total = 0
#     shop_count = 0
#     cart = request.session.get('cart', {})

#     for item_id, quantity in cart.items():
#         shop = get_object_or_404(Shop, pk=item_id)
#         total += quantity * shop.price
#         shop_count += quantity
#         cart_items.append({
#             'item_id': item_id,
#             'quantity': quantity,
#             'shop': shop,
#         })

#     delivery = 2.99
    
#     grand_total = delivery + total
    
#     context = {
#         'cart_items': cart_items,
#         'total': total,
#         'shop_count': shop_count,
#         'delivery': delivery,
#         'grand_total': grand_total,
#     }

#     return context

def cart(request):
    return{'cart': Cart(request)}