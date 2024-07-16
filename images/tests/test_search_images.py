from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image as IMG
from albums.models import Album
from images.models import Image
from users.models import User
import tempfile


# Tests para la búsqueda de imagenes
class SearchImagesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('search_images')
        self.user = User.objects.create(
            username='Test Username',
            email='test@email.com',
            password='TestPassword'
        )
        self.client.force_authenticate(user=self.user)


    # Crear una imagen temporal para las pruebas
    def create_test_image(self):
        image = IMG.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(temp_file, format='PNG')
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/png')


    # Prueba de buscar imagenes exitosamente
    def test_search_images_successful(self):
        self.url += '?query=Test Image Title'
        Image.objects.create(title='Test Image Title', image=self.create_test_image(), user=self.user)
        Image.objects.create(image=self.create_test_image(), user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de buscar imagenes sin token
    def test_search_images_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
