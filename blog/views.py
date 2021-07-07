from django.shortcuts import render
from .models import Post
from .forms import CommentForm



def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all().order_by('-id')
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/post.html', context)
