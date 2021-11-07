from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status

from profiles.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated, *args, **kwargs):
        password = validated.pop("password", None)
        if not password:
            raise ValidationError({"message": "Need password"}, code=status.HTTP_400_BAD_REQUEST) # noqa
        user = User.objects.create(**validated)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
