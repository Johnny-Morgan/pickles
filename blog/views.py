from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all().order_by('-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post', slug=post.slug)
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/post.html', context)
