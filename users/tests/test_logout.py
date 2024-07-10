from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from users.models import User


# Tests para el cierre de sesión
class LogoutTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('logout')
        self.user = User.objects.create(
            username='Test Username',
            email='test@email.com',
            password='TestPassword'
        )
        self.client.force_authenticate(user=self.user)


    # Prueba de cierre de sesión exitoso
    def test_logout_successful(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de cierre de sesión sin token
    def test_logout_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
