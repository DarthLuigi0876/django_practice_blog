from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib import admin
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name="blog_home"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('about/', views.about, name="blog_about")
]