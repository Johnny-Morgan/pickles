from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm


def blog(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title)
            post.save()
            return redirect('blog')
    else:
        form = PostForm()

    context = {'posts': posts, 'form': form}
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


def edit_post(request, slug):
    """ View to edit a blog post """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            post.slug = slugify(post.title)
            post.save()
            return redirect(reverse('post', args=[post.slug]))
    else:
        form = PostForm(instance=post)
    context = {'post': post, 'form': form}

    return render(request, 'blog/edit_post.html', context)


def delete_post(request, post_id):
    """ View to delete a blog post """
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    return redirect(reverse('blog'))