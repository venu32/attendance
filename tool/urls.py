from django.urls import path
from django.contrib import admin
from tool.views import ResetPasswordView
from . import views
# from .views import login_user
from django.contrib.auth import views as auth_views

urlpatterns = [
   # path('', views.home, name ="home"),
    # path('login/', views.login_user, name='login'),
    # path('', views.home, name ="home"),
    path('', views.login_user, name ='login'),
    path('attend', views.attend, name='attend'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('insert', views.insert, name='insert'),
    path('inserts', views.inserts, name='inserts'),
    path('registeration', views.registeration ,name="registeration"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('admin', views.admin, name='admin'),
    path('home', views.home, name ="home"),
    path('basepage', views.basepage, name ="basepage"),
    path('edit/<id>', views.edit, name='edit'),
]