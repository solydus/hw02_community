from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('group/', views.group),
    path('group_post/', views.group),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:pk>/', views.postdetail.as_view(), name='posts_detail'),
    path('posts/<int:pk>/update', views.postupdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.postdelete.as_view(), name='posts_delete'),
    path('create/', views.create, name='create'),
]
