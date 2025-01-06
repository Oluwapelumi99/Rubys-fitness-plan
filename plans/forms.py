from .models import MealPlan, Exercise
# from .widgets import CustomClearableFileInput
from django import forms


class MealPlanForm(forms.ModelForm):


    class Meta:
        model = MealPlan
        fields = ('name','slug','image','description','calories')


    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


class ExerciseForm(forms.ModelForm):


    class Meta:
        model = Exercise
        fields = '__all__'