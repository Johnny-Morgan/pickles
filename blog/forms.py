from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'body': 'Your Comment',
        }
