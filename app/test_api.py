import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    return User.objects.create_user(username='testuser', password='12345')

def test_create_post_authenticated(api_client, create_user):
    user = create_user
    api_client.force_authenticate(user=user)
    response = api_client.post('/api/posts/', {'title': 'New Post', 'info': 'Post information', 'userId': user.id})
    assert response.status_code == 201

def test_create_post_unauthenticated(api_client):
    response = api_client.post('/api/posts/', {'title': 'New Post', 'info': 'Post information'})
    assert response.status_code == 403