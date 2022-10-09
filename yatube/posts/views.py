from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.urls import is_valid_path
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

from .models import Group, Post, User

User = get_user_model()

POST_V = 10


def index(request):
    """Выводим на страницу первые 10 записей постов."""
#    posts = Post.objects.select_related('author')[:POST_V]
    post_list = Post.objects.all().order_by("-pub_date") 
    paginator = Paginator(post_list, 10) 
    page_number = request.GET.get('page')
    template = 'posts/index.html'
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group(request):
    template = 'posts/group_list.html'
    return render(request, template)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_V]
    return render(request, "posts/group_list.html",
                  {"group": group, "posts": posts})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.postyy.select_related()
    context = {
        'author': author,
        'posts': posts
                }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'posts/post_detail.html', context)


class postdetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post_detail'


class postupdate(UpdateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['text', 'group', 'author']
    context_object_name = 'post_update'


class postdelete(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    fields = ['text', 'group', 'author']
    context_object_name = 'post_delete'
    success_url = '/'


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "SHIT"
    form = PostForm()
     
    data_form = {'form': form}
    success_url = '/'

    return render(request, 'posts/create.html', data_form)