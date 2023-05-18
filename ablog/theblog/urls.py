
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ArticleDetailView, AddPostView
from . import views

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),

]