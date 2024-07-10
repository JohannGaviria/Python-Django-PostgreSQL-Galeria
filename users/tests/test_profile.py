from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from users.models import User


# Tests para el perfil de usuario
class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('profile')
        self.existing_user = User.objects.create(
            username='Test Existing Username',
            email='testexisting@email.com'
        )
        self.existing_user.set_password('TestExistingPassword')
        self.user = User.objects.create(
            username='Test Username',
            email='test@email.com',
        )
        self.user.set_password('TestPassword')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.data = {
            'username': 'Test Updated Username',
            'email': 'testupdated@email.com',
            'password': 'TestUpdatedPassword'
        }


    # Prueba de obtención de perfil exitoso
    def test_get_profile_successful(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtención de perfil sin autenticación
    def test_get_profile_without_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    # Prueba de actualización de perfil exitosa
    def test_update_profile_successful(self):
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de actualización de perfil con datos inválidos
    def test_update_profile_invalid_data(self):
        self.data['username'] = ''
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de actualización con nombre de usuario existente
    def test_update_existing_username(self):
        self.data['username'] = 'Test Existing Username'
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de actualización con correo electrónico existente
    def test_update_existing_email(self):
        self.data['email'] = 'testexisting@email.com'
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de actualización de perfil sin token
    def test_update_profile_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de eliminación de perfil exitosa
    def test_delete_profile_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de eliminación de perfil sin token
    def test_delete_profile_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        