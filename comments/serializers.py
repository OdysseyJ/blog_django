from comments.models import Comment
from posts.models import Post

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField()
    parent_id = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ['post_id', 'parent_id', 'description']
        extra_kwargs = {
          'post_id': {'required': True, 'allow_null': False},
          'parent_id': {'required': False, 'allow_null': True},
          'description': {'required': True, 'allow_blank': False},
        }

    def create(self, validated, *args, **kwargs):
        user = self.context["request"]._user
        post_id = validated.get('post_id')
        description = validated.get('description')
        parent_id = validated.get('parent_id', None)

        post = Post.objects.filter(id=post_id).first()
        if not post:
            raise Exception("Wrong post_id")

        comment = Comment.objects.create(description=description, post=post, writer=user) # noqa
        if parent_id:
            parent_comment = Comment.objects.filter(id=parent_id).first()
            if not parent_comment:
                raise Exception("Wrong parent_id")

            # NOTE : only depth 1 allowed
            if parent_comment.parents.exists():
                raise Exception("Comment already have parent")

            parent_comment.children.add(comment)

        return comment
