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
def user_b(db) -> User:
    user = User.objects.create_user(
        username="B",
        password="secret",
        first_name="Baloo",
        last_name="Doe",
        email="baloo@gmail.com",
        is_staff=False,
        is_superuser=False,
        is_active=True,
    )
    return user


@pytest.fixture
def user_c(db) -> User:
    user = User.objects.create_user(
        username="C",
        password="secret",
        first_name="Lucas",
        last_name="Doe",
        email="lucas@gmail.com",
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


@pytest.fixture
def vendor_john(db) -> UserProfile:
    vendor = UserProfile(
        user=user_b,
        profile=Profile.VENDOR.value,
    )
    return vendor


@pytest.fixture
def dealer_maria(db) -> UserProfile:
    dealer = UserProfile(
        user=user_c,
        profile=Profile.DEALER.value,
    )
    return dealer
