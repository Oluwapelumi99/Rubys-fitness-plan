from django.shortcuts import render
from .models import Shop
# Create your views here.

def view_shop(request):
    """ A view to return the shopping page """
    shops = Shop.objects.all()
    context = {
        'shops': shops
    }
    return render(request, 'shop/shop.html', context)
