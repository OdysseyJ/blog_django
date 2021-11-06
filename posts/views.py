from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import CursorPagination
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from blog_crud.permissions import IsWriterOrReadOnly


class PostCursorPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = '-created_at'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostCursorPagination
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsWriterOrReadOnly
    ]
