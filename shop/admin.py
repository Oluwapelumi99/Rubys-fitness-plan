from django.contrib import admin
from .models import Shop, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Shop)