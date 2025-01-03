from .models import MealPlan
# from .widgets import CustomClearableFileInput
from django import forms


class MealPlanForm(forms.ModelForm):


    class Meta:
        model = MealPlan
        fields = ('name','slug','image','description','calories')


    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('content',)