from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')  # Order by latest first
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostBySlugAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
