from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Blog, Comment
from .forms import CommentForm

# Create your views here.

class BlogList(generic.ListView):
    queryset = Blog.objects.all()
    template_name = "community/blog_list.html"
    paginate_by = 6

def community(request, slug):
    """ A view to return the community page """
    queryset = Blog.objects.all()
    blog = get_object_or_404(queryset, slug=slug)
    comments = blog.comments.all().order_by("-created_on")
    comment_count = blog.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            blog = comment.blog
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(request, 'community/community.html', 
    {'blog': blog,
    "comments": comments,
    "comment_count": comment_count,
    "comment_form": comment_form,})