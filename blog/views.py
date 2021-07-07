from django.shortcuts import render
from .models import Post


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/post.html', context)
