import pytest

from posts.serializers import PostSerializer

pytestmark = pytest.mark.django_db


class TestPostSerializer:

    def test_serialize_model(self, temp_dummy_posts):
        post = temp_dummy_posts(1)[0]
        serializer = PostSerializer(post)

        assert serializer.data

    def test_serialized_data(self, temp_dummy_posts):
        post = temp_dummy_posts(1)[0]
        serializer = PostSerializer(data=post.__dict__)

        assert serializer.is_valid()
        assert serializer.errors == {}
