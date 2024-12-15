from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shop, name='shop'),
    path('<shop_id>', views.item_details, name='item_details'),
]