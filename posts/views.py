from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from blog_crud.permissions import IsWriterOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsWriterOrReadOnly
    ]

    def create(self, req):
        print("########################## viewset")
        print(req.__dict__)
        super(PostViewSet, self).create(req)
