import pytest

from posts.models import Post


pytestmark = pytest.mark.django_db


class TestPostModel:

    def test_soft_delete(self, saved_dummy_posts):
        post = saved_dummy_posts(1)[0]
        find = Post.objects.filter(id=post.id).first()
        assert find.id == post.id

        post.delete(soft_delete=True)
        find = Post.objects.filter(id=post.id).first()
        assert find is None

        find = Post.objects.filter(
            deleted_at__isnull=False,
            id=post.id
        ).first()
        assert find is None
