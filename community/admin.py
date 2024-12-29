from django.contrib import admin
from .models import Blog, Comment, Reply
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)
admin.site.register(Reply)