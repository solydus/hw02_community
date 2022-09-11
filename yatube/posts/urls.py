from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('group/', views.group),
    path('group_post/', views.group),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
