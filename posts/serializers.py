from posts.models import Post

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description']

    def create(self, validated, *args, **kwargs):
        user = self.context["request"]._user
        return Post.objects.create(**validated, writer=user)
