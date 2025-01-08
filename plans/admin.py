from django.contrib import admin
from .models import GlutesExercise, AbsExercise, MealPlan
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(GlutesExercise)
class ExerciseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')


@admin.register(AbsExercise)
class ExerciseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')


@admin.register(MealPlan)
class MealPlanAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)