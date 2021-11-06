from django.contrib.auth.models import User
from django.db import transaction
from django.utils.decorators import method_decorator

from rest_framework import viewsets

from blog_crud.serializers import UserSerializer


class Atomic(object):
    @method_decorator(transaction.atomic)
    def dispatch(self, request, *args, **kwargs):
        return super(Atomic, self).dispatch(request, *args, **kwargs)


class ModelViewSet(Atomic, viewsets.ModelViewSet):
    pass


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        #  IsOwnerOrReadOnly
    ]
