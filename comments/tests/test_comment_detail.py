from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image as IMG
from comments.models import Comment
from images.models import Image
from users.models import User
import tempfile


# Tests para la obtención, actualización y eliminacion de comentario
class CommentDetailTestCase(TestCase):
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
        self.comment = Comment.objects.create(
            comment='Test Comment',
            image=self.image,
            user=self.user
        )
        self.url = reverse('comment_detail', args=[self.comment.id])
        self.invalid_url = reverse('image_detail', args=[999])
        self.update_data = {
            'comment': 'Test Updated Comment',
            'image': self.image.id,
            'user': self.user.id
        }


    # Crear un comentario temporal para las pruebas
    def create_test_image(self):
        image = IMG.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(temp_file, format='PNG')
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/png')


    # Prueba de obtener un comentario exitosamente
    def test_get_comment_successful(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de obtener un comentario inexistente
    def test_get_nonexistent_comment(self):
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener un comentario sin token
    def test_get_comment_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de actualizar un comentario exitosamente
    def test_update_comment_successful(self):
        response = self.client.put(self.url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba de actualizar un comentario con datos inválidos
    def test_update_comment_invalid_data(self):
        invalid_data = {
            'comment': '',
            'image': self.image.id,
            'user': self.user.id
        }
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de actualizar un comentario inexistente
    def test_update_nonexistent_comment(self):
        response = self.client.put(self.invalid_url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba de obtener un comentario sin token
    def test_updated_comment_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # Prueba de eliminar un comentario exitosamente
    def test_delete_comment_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba de eliminar un comentario inexistente
    def test_delete_nonexistent_comment(self):
        response = self.client.delete(self.invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)

    
    # Prueba de obtener un comentario sin token
    def test_delete_comment_without_token(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
