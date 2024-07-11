from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from albums.models import Album
from users.models import User


# Tests para la obtención y creación de álbumes
class AlbumListCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('album_list_create')
        self.user = User.objects.create(
            username='Test Username',
            email='test@email.com',
            password='TestPassword'
        )
        self.client.force_authenticate(user=self.user)
        
        self.data = {
            'name': 'Test Album Name',
            'description': 'Test Album Description',
            'visibility': True,
            'user': self.user.id
        }
    

    # Prueba de obtener álbumes exitosamente
    def test_get_albums_successful(self):
        Album.objects.create(user=self.user, name='Test Album 1', description='Test Description 1', visibility=True)
        Album.objects.create(user=self.user, name='Test Album 2', description='Test Description 2', visibility=False)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener álbumes cuando el usuario no tiene álbumes creados
    def test_get_albums_no_albums(self):
        Album.objects.filter(user=self.user.id).delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener álbum sin token
    def test_get_album_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

    # Prueba de crear un álbum exitosamente
    def test_create_album_successful(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de crear un álbum con datos inválidos
    def test_create_album_invalid_data(self):
        del self.data['name']
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de crear álbum sin token
    def test_create_album_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
