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


# Tests para la obtención y creación de imagenes
class ImageListCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('image_list_create')
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
        image = self.create_test_image()
        self.data = {
            'title': 'Test Image Title',
            'description': 'Test Image Description',
            'image': image,
            'user': self.user.id,
            'album': self.album.id
        }


    # Crear una imagen temporal para las pruebas
    def create_test_image(self):
        image = IMG.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(temp_file, format='PNG')
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/png')


    # Prueba de obtener imagenes exitosamente
    def test_get_image_successful(self):
        Image.objects.create(image=self.create_test_image(), user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener imagenes cuando el usuario no tiene imagenes agregadas
    def test_get_images_no_images(self):
        Album.objects.filter(user=self.user.id).delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener imagenes sin token
    def test_get_image_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

    # Prueba de crear una imagen exitosamente
    def test_create_image_successful(self):
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de crear una imagen con datos inválidos
    def test_create_image_invalid_data(self):
        del self.data['image']
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de crear una imagen sin token
    def test_create_image_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
