import pytest

from django.contrib.auth.models import User
from model_bakery import baker

from posts.models import Post


@pytest.fixture
def saved_dummy_posts():
    def posts_bakery_batch(n):
        writer = User.objects.filter(username="test").first()
        if not writer:
            writer = baker.make(
                User,
                email="test@test.com",
                username="test",
                password="test123"
            )
        posts = baker.make(
            Post,
            _fill_optional=[
                'title',
                'description',
            ],
            _quantity=n,
            writer=writer
        )
        return posts
    return posts_bakery_batch


@pytest.fixture
def temp_dummy_posts():
    def posts_bakery_batch(n):
        writer = User.objects.filter(username="test").first()
        if not writer:
            writer = baker.prepare(
                User,
                email="test@test.com",
                username="test",
                password="test123"
            )
        posts = baker.prepare(
            Post,
            _fill_optional=[
                'id',
                'title',
                'description',
                'writer',
            ],
            _quantity=n,
            writer=writer
        )
        return posts
    return posts_bakery_batch
