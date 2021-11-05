from django.db import models
from blog_crud.models import Model
from django.contrib.auth.models import User


class Post(Model):
    title = models.CharField(
        'Title', db_index=True, max_length=100,
    )
    description = models.TextField('Description', blank=True)
    writer = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
