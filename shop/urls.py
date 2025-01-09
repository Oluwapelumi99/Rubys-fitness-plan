from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shop, name='shop'),
    path('<shop_id>', views.item_details, name='item_details'),
    path('add/', views.add_items, name='add_items'),
    path('edit/<int:shop_id>/', views.edit_items, name='edit_items'),
    path('delete/<int:shop_id>/', views.delete_items, name='delete_items'),
]
