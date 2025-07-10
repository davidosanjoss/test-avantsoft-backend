import pytest

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .conftest import ClientFactory, SaleFactory

User = get_user_model()


@pytest.fixture
def api_client():
    user = User.objects.create_user(username='testuser', password='testpass')
    refresh = RefreshToken.for_user(user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
    return client
