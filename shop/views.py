from django.shortcuts import render, get_object_or_404
from .models import Shop
# Create your views here.

def view_shop(request):
    """ A view to return the shopping page """
    shops = Shop.objects.all()
    context = {
        'shops': shops
    }
    return render(request, 'shop/shop.html', context)


def item_details(request, shop_id):
    """ A view to return individul item details"""
    shop = get_object_or_404(Shop, pk=shop_id)
    context = {
        'shop': shop
    }
    return render(request, 'shop/item_details.html', context)