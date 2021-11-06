from django.db import models
from django.contrib.auth.models import User

from posts.models import Post
from blog_crud.models import Model


class Comment(Model):
    writer = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # NOTE : only depth 1 allowed in serializer
    children = models.ManyToManyField('self', symmetrical=False, related_name='parents') # noqa
    description = models.TextField('Description', blank=True)
    writer = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

    class Meta:
        ordering = ['-created_at']
