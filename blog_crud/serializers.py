from django.contrib.auth.models import User

from rest_framework import serializers

from profiles.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, validated, *args, **kwargs):
        user = User.objects.create(**validated)
        Profile.objects.create(user=user)
        return user
