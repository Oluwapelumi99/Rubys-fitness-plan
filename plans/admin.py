from django.contrib import admin
from .models import Exercise, MealPlan
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description','abs_description',)


@admin.register(MealPlan)
class MealPlanAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)