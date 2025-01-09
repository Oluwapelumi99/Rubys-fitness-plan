from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Shop, Category
from .forms import ShopForm
# Create your views here.


def view_shop(request):
    """ A view to return all shopping list,
    including sorting and search queries  """

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

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
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


@login_required
def add_items(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('item_details', args=[shop.id]))
        else:
            messages.error(
                request,
                'Failed to add item. Please ensure the form is valid.')
    else:
        form = ShopForm()

    template = 'shop/add_items.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_items(request, shop_id):
    """ Edit an item in the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorized personnel can do this.')
        return redirect(reverse('home'))

    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('item_details', args=[shop.id]))
        else:
            messages.error(
                request,
                'Failed to update item. Please ensure the form is valid.')
    else:
        form = ShopForm(instance=shop)
        messages.info(request, f'You are editing {shop.name}')

    template = 'shop/edit_items.html'
    context = {
        'form': form,
        'shop': shop,
    }

    return render(request, template, context)


@login_required
def delete_items(request, shop_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Authorized personnel only.')
        return redirect(reverse('home'))

    shop = get_object_or_404(Shop, pk=shop_id)
    shop.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('shop'))
