import pytest
import json


pytestmark = pytest.mark.django_db


class TestPostEndpoints:

    endpoint = '/posts/'

    def test_list_without_token(self, api_client, saved_dummy_posts):
        saved_dummy_posts(3)

        response = api_client.get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_list(self, authorized_client, saved_dummy_posts):
        saved_dummy_posts(3)

        response = authorized_client.get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create_without_token(self, api_client, temp_dummy_posts):
        post = temp_dummy_posts(1)[0]
        expected = {
            'title': post.title,
            'description': post.description
        }

        response = api_client.post(
            self.endpoint,
            data=expected,
            format='json'
        )

        assert response.status_code == 401

    def test_create(self, authorized_client, temp_dummy_posts):
        post = temp_dummy_posts(1)[0]
        expected = {
            'title': post.title,
            'description': post.description
        }

        response = authorized_client.post(
            self.endpoint,
            data=expected,
            format='json'
        )

        response_data = json.loads(response.content)
        response_data.pop("id")

        assert response.status_code == 201
        assert response_data == expected

    def test_retrieve_without_token(self, api_client, saved_dummy_posts):
        post = saved_dummy_posts(1)[0]
        expected = {
            'title': post.title,
            'description': post.description
        }

        url = f'{self.endpoint}{post.id}/'
        response = api_client.get(url)
        response_data = json.loads(response.content)
        response_data.pop("id")

        assert response.status_code == 200
        assert response_data == expected

    def test_retrieve(self, authorized_client, saved_dummy_posts):
        post = saved_dummy_posts(1)[0]
        expected = {
            'title': post.title,
            'description': post.description
        }

        url = f'{self.endpoint}{post.id}/'
        response = authorized_client.get(url)
        response_data = json.loads(response.content)
        response_data.pop("id")

        assert response.status_code == 200
        assert response_data == expected

    def test_update_without_token(self, api_client, saved_dummy_posts, temp_dummy_posts): # noqa
        old_post = saved_dummy_posts(1)[0]
        new_post = temp_dummy_posts(1)[0]
        expected = {
            'title': new_post.title,
            'description': new_post.description
        }

        url = f'{self.endpoint}{old_post.id}/'
        response = api_client.put(
            url,
            expected,
            format="json"
        )

        assert response.status_code == 401

    def test_update(self, authorized_client, saved_dummy_posts, temp_dummy_posts): # noqa
        old_post = saved_dummy_posts(1)[0]
        new_post = temp_dummy_posts(1)[0]
        expected = {
            'title': new_post.title,
            'description': new_post.description
        }

        url = f'{self.endpoint}{old_post.id}/'
        response = authorized_client.put(
            url,
            expected,
            format="json"
        )
        response_data = json.loads(response.content)
        response_data.pop("id")

        assert response.status_code == 200
        assert response_data == expected

    @pytest.mark.parametrize('field', [
        ('title'),
        ]
    )
    def test_partial_update(self, field, authorized_client, saved_dummy_posts, temp_dummy_posts): # noqa
        old_post = saved_dummy_posts(1)[0]
        new_post = temp_dummy_posts(1)[0]
        expected = {
            'title': old_post.title,
            'description': old_post.description
        }
        partial = getattr(new_post, field)
        url = f'{self.endpoint}{old_post.id}/'
        response = authorized_client.put(
            url,
            {field: partial},
            format="json"
        )
        response_data = json.loads(response.content)
        response_data.pop("id")

        assert response.status_code == 200
        assert response_data == {**expected, **{field: partial}}

    def test_delete_without_token(self, api_client, saved_dummy_posts):
        post = saved_dummy_posts(1)[0]

        url = f'{self.endpoint}{post.id}/'
        response = api_client.delete(url)

        assert response.status_code == 401

    def test_delete(self, authorized_client, saved_dummy_posts):
        post = saved_dummy_posts(1)[0]

        url = f'{self.endpoint}{post.id}/'
        response = authorized_client.delete(url)

        assert response.status_code == 204
