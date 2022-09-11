from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POST_V = 10


def index(request):
    """Выводим на страницу первые 10 записей постов."""
    posts = Post.objects.select_related('author')[:POST_V]
    template = 'posts/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def group(request):
    template = 'posts/group_list.html'
    return render(request, template)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_V]
    return render(request, "posts/group_list.html",
                   {"group": group, "posts": posts})
