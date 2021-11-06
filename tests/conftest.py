import pytest

from model_bakery import baker
from django.contrib.auth.models import User

from rest_framework.test import APIClient


pytestmark = [pytest.mark.unit]


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authorized_client():
    user = User.objects.filter(username="test").first()
    if not user:
        user = baker.make(
            User,
            email="test@test.com",
            username="test",
            password="test123"
        )
    client = APIClient()
    client.force_authenticate(user=user)
    return client
