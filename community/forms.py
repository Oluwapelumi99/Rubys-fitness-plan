from .models import Comment, Reply
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)