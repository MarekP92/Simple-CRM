import pytest

from django.contrib.auth.models import User, Group


@pytest.fixture
def default_group_fixture(db):
    Group.objects.create(name='customers')
    Group.objects.create(name='admin')


@pytest.mark.django_db
def test_user_with_default_group_fixture(db):
    user = User.objects.create_user(
       'john', 'lennon@thebeatles.com', 'johnpassword',

    )
    assert user
    assert user.groups.filter(name='customers')
    assert user.groups.filter(name='admin')

