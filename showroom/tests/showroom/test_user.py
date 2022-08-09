import pytest

from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        username='admin',
        password='1234'
    )
    url = '/api/v1/users/login'
    response = client.post(url, payload)

    assert response.status_code == 200
