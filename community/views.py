from django.shortcuts import render
from .models import Blog, Comment

# Create your views here.

def community(request):
    """ A view to return the community page """
    blogs = Blog.objects.all()
    return render(request, 'community/community.html', {'blogs': blogs})