from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Shop
# Create your views here.

def view_shop(request):
    """ A view to return all shopping list,  including sorting and search queries  """

    shops = Shop.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria!")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            shops = shops.filter(queries)
    context = {
        'shops': shops,
        'search_term': query,
    }
    return render(request, 'shop/shop.html', context)


def item_details(request, shop_id):
    """ A view to return individul item details"""
    shop = get_object_or_404(Shop, pk=shop_id)
    context = {
        'shop': shop
    }
    return render(request, 'shop/item_details.html', context)