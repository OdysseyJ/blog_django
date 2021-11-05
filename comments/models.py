from django.db import models
from blog_crud.models import Model
from profiles.models import Profile


class CommentMixin(Model):
    description = models.TextField('Description', blank=True)
    writer = models.ForeignKey(Profile, on_delete=models.deletion.CASCADE)

    class Meta:
        abstract = True


class Comment(CommentMixin):
    # NOTE : not using children because of ease of implementation
    #  children = models.ManyToManyField('self', symmetric=False)
    pass


class SubComment(CommentMixin):
    pass
