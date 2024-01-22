from django.shortcuts import render
from rest_framework import generics
from posts.models import Post
from posts.serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer