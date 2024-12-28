from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Blog, Comment

# Create your views here.

class BlogList(generic.ListView):
    queryset = Blog.objects.all()
    template_name = "community/blog_list.html"
    paginate_by = 6

def community(request, slug):
    """ A view to return the community page """
    queryset = Blog.objects.all()
    blog = get_object_or_404(queryset, slug=slug)
    return render(request, 'community/community.html', {'blog': blog})