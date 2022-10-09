from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('pass/', LogoutView.as_view(template_name='users/logged_out.html'), name='password_reset_form'),
    path('password_change/', PasswordResetView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]
