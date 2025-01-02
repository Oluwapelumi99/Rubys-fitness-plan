from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Shop, Category
# Create your views here.

def view_shop(request):
    """ A view to return all shopping list,  including sorting and search queries  """

    shops = Shop.objects.all()
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                shops = shops.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            shops = shops.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            shops = shops.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria!")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            shops = shops.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'shops': shops,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }
    
    return render(request, 'shop/shop.html', context)


def item_details(request, shop_id):
    """ A view to return individul item details"""
    shop = get_object_or_404(Shop, pk=shop_id)
    context = {
        'shop': shop
    }
    return render(request, 'shop/item_details.html', context)