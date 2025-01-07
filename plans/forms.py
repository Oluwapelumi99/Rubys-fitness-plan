from .models import MealPlan, Exercise
# from .widgets import CustomClearableFileInput
from django import forms


class MealPlanForm(forms.ModelForm):


    class Meta:
        model = MealPlan
        fields = ('name','slug','image','description','calories')


    image = forms.ImageField(label='Image', required=False,)


class ExerciseForm(forms.ModelForm):


    class Meta:
        model = Exercise
        fields = '__all__'


class DeleteExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = []

    def __init__(self, *args, **kwargs):
        super(DeleteExerciseForm, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(widget=forms.HiddenInput())
        if self.instance and self.instance.pk:
            self.fields['id'].initial = self.instance.pk