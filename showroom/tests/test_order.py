import pytest
from django.contrib.auth.models import User

from users.models import UserProfile
from core.enums import Profile


@pytest.fixture
def user_a(db) -> User:
    user = User.objects.create_user(
        username="A",
        password="secret",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
        is_staff=False,
        is_superuser=False,
        is_active=True,
    )
    return user


@pytest.fixture
def customer_alex(db) -> UserProfile:
    customer = UserProfile(
        user=user_a,
        profile=Profile.CUSTOMER.value,
    )
    return customer


def test_should_create_user_with_username(db) -> None:
    assert user_a.username == 'A'
