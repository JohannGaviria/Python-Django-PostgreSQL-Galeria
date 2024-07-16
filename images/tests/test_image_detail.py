from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image as IMG
from images.models import Image
from users.models import User
import tempfile


# Tests para la obtención, actualización y eliminacion de imagenes
class ImageDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='Test Username',
            email='test@email.com',
            password='TestPassword'
        )
        self.client.force_authenticate(user=self.user)
        image = self.create_test_image()
        self.image = Image.objects.create(
            title='Test Image Title',
            description='Test Image Description',
            image=image,
            user=self.user
        )
        self.url = reverse('image_detail', args=[self.image.id])
        self.invalid_url = reverse('image_detail', args=[999])
        update_image = self.create_test_image()
        self.update_data = {
            'title': 'Updated Image Title',
            'description': 'Updated Image Description',
            'image': update_image,
            'user': self.user.id
        }


    # Crear una imagen temporal para las pruebas
    def create_test_image(self):
        image = IMG.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(temp_file, format='PNG')
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/png')


    # Prueba de obtener una imagen exitosamente
    def test_get_imagen_successful(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener una imagen inexistente
    def test_get_nonexistent_image(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener una imagen sin token
    def test_get_image_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de actualizar una imagen exitosamente
    def test_update_image_successful(self):
        response = self.client.put(self.url, self.update_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de actualizar una imagen con datos inválidos
    def test_update_image_invalid_data(self):
        invalid_data = {
            'name': '',
            'description': 'Updated Album Description',
            'visibility': False,
        }
        response = self.client.put(self.url, invalid_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de actualizar una imagen inexistente
    def test_update_nonexistent_image(self):
        response = self.client.put(self.invalid_url, self.update_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener una imagen sin token
    def test_updated_image_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de eliminar una imagen exitosamente
    def test_delete_image_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de eliminar una imagen inexistente
    def test_delete_nonexistent_image(self):
        response = self.client.delete(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)

    
    # Prueba de obtener una imagen sin token
    def test_delete_image_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
