from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        print(cleaned_data)
        author = cleaned_data.get['author']
        comment = data.get['comment']
        return cleaned_data
