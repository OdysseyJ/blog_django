from posts.models import Post

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'writer']

    def create(self, validated):
        print("##########################")
        print(validated)
        super(PostSerializer, self).create(validated)
