from django.urls import path, include
from .views import PostListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='task-list-create'),
]