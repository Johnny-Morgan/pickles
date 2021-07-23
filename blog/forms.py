from django import forms
from .widgets import CustomClearableFileInput
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'body': 'Your Comment',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'author']

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)