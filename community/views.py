from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Blog, Comment, Reply
from .forms import CommentForm, ReplyForm

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
    replies = Reply.objects.filter(comment__in=comments)
    comment_count = blog.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Blog.objects.all()
        blog = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('community', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Blog.objects.all()
    blog = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('community', args=[slug]))


def reply(request, slug, pk):
    comments = Comment.objects.filter(blog=blog)
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        reply_form = ReplyForm(data=request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.save()
            return redirect('community', pk=comment.blog.pk)
    else:
        reply_form = ReplyForm()
    return render(request, 'community/community.html', {'reply_form': reply_form,})