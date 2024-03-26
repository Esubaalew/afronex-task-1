from django.shortcuts import render
from .models import Post
from .forms import PostForm

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')  # Order by latest first
    serializer_class = PostSerializer
