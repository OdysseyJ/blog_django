from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import CursorPagination

from comments.models import Comment
from comments.serializers import CommentSerializer
from blog_crud.permissions import IsWriterOrReadOnly
from blog_crud.views import ModelViewSet


class CommentCursorPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = '-created_at'


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentCursorPagination
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsWriterOrReadOnly
    ]
