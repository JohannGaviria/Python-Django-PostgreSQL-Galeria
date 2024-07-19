from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image as IMG
from images.models import Image
from users.models import User
from comments.models import Comment
import tempfile


# Tests para la obtención y creación de comentarios de imagenes
class CommentListCreateTestCase(TestCase):
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
        self.url = reverse('comment_list_create', args=[self.image.id])
        self.data = {
            'comment': 'Test Comment Image',
            'image': self.image.id,
            'user': self.user.id
        }


    # Crear una imagen temporal para las pruebas
    def create_test_image(self):
        image = IMG.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(temp_file, format='PNG')
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/png')


    # Prueba de obtener comentarios exitosamente
    def test_get_comment_successful(self):
        Comment.objects.create(comment='Test Comment', image=self.image, user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener comentarios cuando la imagen no tiene comentarios
    def test_get_comments_without_comments_images(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener comentarios sin token
    def test_get_comment_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

    # Prueba de crear un comentario exitosamente
    def test_create_comment_successful(self):
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de crear un comentario con datos inválidos
    def test_create_comment_invalid_data(self):
        del self.data['comment']
        response = self.client.post(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de crear un comentario sin token
    def test_create_comment_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
