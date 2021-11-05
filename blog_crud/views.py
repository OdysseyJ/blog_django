from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from blog_crud.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        #  IsOwnerOrReadOnly
    ]
