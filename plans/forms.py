from .models import MealPlan, GlutesExercise, AbsExercise
from django import forms


class MealPlanForm(forms.ModelForm):


    class Meta:
        model = MealPlan
        fields = ('name','slug','image','description','calories')



class GlutesExerciseForm(forms.ModelForm):


    class Meta:
        model = GlutesExercise
        fields = '__all__'


class AbsExerciseForm(forms.ModelForm):


    class Meta:
        model = AbsExercise
        fields = '__all__'



class DeleteGlutesExerciseForm(forms.ModelForm):
    class Meta:
        model = GlutesExercise
        fields = []

    def __init__(self, *args, **kwargs):
        super(DeleteGlutesExerciseForm, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(widget=forms.HiddenInput())
        if self.instance and self.instance.pk:
            self.fields['id'].initial = self.instance.pk

class DeleteAbsExerciseForm(forms.ModelForm):
    class Meta:
        model = AbsExercise
        fields = []

    def __init__(self, *args, **kwargs):
        super(DeleteAbsExerciseForm, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(widget=forms.HiddenInput())
        if self.instance and self.instance.pk:
            self.fields['id'].initial = self.instance.pk