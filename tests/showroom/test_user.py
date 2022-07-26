import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_auth_user():
    payload = dict(
        username='admin',
        password='1234'
    )

    response = client.post('/api/v1/users/login', payload)

    assert response.status_code == 200
