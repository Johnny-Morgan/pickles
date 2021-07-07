from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Comment
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


def delete_comment(request, comment_id):
    """ Delete a comment from a blog post """
    if not request.user.is_superuser:
        return redirect(reverse('blog'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect(reverse('blog'))
