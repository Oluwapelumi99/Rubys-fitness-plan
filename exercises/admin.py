from django.contrib import admin
from .models import Exercise
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description','abs_description',)
