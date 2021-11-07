from django.contrib.auth.models import User
from django.db import transaction
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, views, status

from blog_crud.serializers import UserSerializer, UserLoginSerializer
from blog_crud.permissions import IsOwnerOrReadOnly
from blog_crud.authentications import token_expire_handler, expires_in


class Atomic(object):
    @method_decorator(transaction.atomic)
    def dispatch(self, request, *args, **kwargs):
        return super(Atomic, self).dispatch(request, *args, **kwargs)


class ModelViewSet(Atomic, viewsets.ModelViewSet):
    pass


class APIView(Atomic, views.APIView):
    pass


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        login_serializer = UserLoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            return Response(
                login_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {'message': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        if not user.is_active:
            return Response(
                {'message': 'User is not active'},
                status=status.HTTP_400_BAD_REQUEST
            )

        login(request, user)
        token = Token.objects.get_or_create(user=user)[0]
        is_expired, token = token_expire_handler(token)
        user_serialized = UserSerializer(user)

        return Response({
            'user': user_serialized.data,
            'expires_in': expires_in(token),
            'token': token.key
        }, status=status.HTTP_200_OK)
