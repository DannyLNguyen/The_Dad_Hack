from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('login_user', views.login_user),
    path('home', views.home),
    path('articles', views.articles),
    path('forum', views.forum),
    path('shop', views.shop),
    path('logout', views.logout)
]