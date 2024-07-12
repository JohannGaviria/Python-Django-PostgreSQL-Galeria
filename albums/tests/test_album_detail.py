from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from albums.models import Album
from users.models import User


# Tests para la obtención, actualización y eliminacion de álbumes
class AlbumDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='Test Username',
            email='test@email.com',
            password='TestPassword'
        )
        self.client.force_authenticate(user=self.user)
        self.album = Album.objects.create(
            name='Test Album Name',
            description='Test Album Description',
            visibility=True,
            user=self.user
        )
        self.url = reverse('album_detail', args=[self.album.id])
        self.invalid_url = reverse('album_detail', args=[999])
        self.update_data = {
            'name': 'Updated Album Name',
            'description': 'Updated Album Description',
            'visibility': False,
            'user': self.user.id
        }


    # Prueba de obtener álbum exitosamente
    def test_get_album_successful(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener álbum inexistente
    def test_get_nonexistent_album(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener álbum sin token
    def test_get_album_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de actualizar álbum exitosamente
    def test_update_album_successful(self):
        response = self.client.put(self.url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de actualizar álbum con datos inválidos
    def test_update_album_invalid_data(self):
        invalid_data = {
            'name': '',
            'description': 'Updated Album Description',
            'visibility': False,
        }
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de actualizar álbum inexistente
    def test_update_nonexistent_album(self):
        response = self.client.put(self.invalid_url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener álbum sin token
    def test_updated_album_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de eliminar álbum exitosamente
    def test_delete_album_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de eliminar álbum inexistente
    def test_delete_nonexistent_album(self):
        response = self.client.delete(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)

    
    # Prueba de obtener álbum sin token
    def test_get_album_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
