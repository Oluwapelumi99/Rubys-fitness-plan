from django import forms
from .models import Shop, Category


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
