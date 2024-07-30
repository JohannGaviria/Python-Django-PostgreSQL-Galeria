from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image as IMG
from likes.models import Like
from images.models import Image
from users.models import User
import tempfile


# Tests para la obtención y eliminación de like
class LikeDetailTestCase(TestCase):
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
        self.like = Like.objects.create(
            like=True,
            image=self.image,
            user=self.user
        )
        self.url = reverse('like_detail', args=[self.like.id])
        self.invalid_url = reverse('like_detail', args=[999])


    # Crear un comentario temporal para las pruebas
    def create_test_image(self):
        image = IMG.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(temp_file, format='PNG')
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/png')


    # Prueba de obtener un like exitosamente
    def test_get_like_successful(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener un like inexistente
    def test_get_nonexistent_like(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener un like sin token
    def test_get_like_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de eliminar un like exitosamente
    def test_delete_like_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de eliminar un like inexistente
    def test_delete_nonexistent_like(self):
        response = self.client.delete(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)

    
    # Prueba de obtener un like sin token
    def test_delete_like_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
