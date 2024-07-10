from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from users.models import User


# Tests para el inicio de sesión
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        user = User.objects.create(
            username='Test Username',
            email='test@email.com'
        )
        user.set_password('TestPassword')
        user.save()
        self.data = {
            'email': 'test@email.com',
            'password': 'TestPassword'
        }


    # Prueba de inicio de sesión exitoso
    def test_login_successful(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de inicio de sesión con correo electrónico inválido
    def test_login_invalid_email(self):
        self.data['email'] = 'incorrect@email.com'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de inicio de sesión con contraseña incorrecta
    def test_login_invalid_password(self):
        self.data['password'] = 'IncorrectPassword'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
