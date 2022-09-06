from django.shortcuts import get_object_or_404, render
from .models import Group, Post

Post_v = 10


def index(request):
    """Выводим на страницу первые 10 записей постов."""
    posts = Post.objects.select_related('author')[:Post_v]
    template = 'posts/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def group(request):
    template = 'posts/group_list.html'
    return render(request, template)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:Post_v]
    return render(request, "posts/post.html", {"group": group, "posts": posts})
