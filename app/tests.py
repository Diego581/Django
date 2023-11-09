from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(userId=self.user, title='Ejemplo', info='Contenido de ejemplo')

    def test_create_comment(self):
        data = {'postId': self.post.id, 'comment': 'Nuevo comentario'}
        response = self.client.post('/api/comments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comment(self):
        comment = Comment.objects.create(userId=self.user, postId=self.post, comment='Ejemplo de comentario')
        response = self.client.get(f'/api/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        comment = Comment.objects.create(userId=self.user, postId=self.post, comment='Comentario original')
        data = {'postId': self.post.id, 'comment': 'Comentario actualizado'}
        response = self.client.put(f'/api/comments/{comment.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        comment = Comment.objects.create(userId=self.user, postId=self.post, comment='Comentario a eliminar')
        response = self.client.delete(f'/api/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        data = {'title': 'Nuevo Post', 'info': 'Contenido del nuevo post'}
        response = self.client.post('/api/posts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_post(self):
        post = Post.objects.create(userId=self.user, title='Ejemplo', info='Contenido de ejemplo')
        response = self.client.get(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        post = Post.objects.create(userId=self.user, title='Ejemplo', info='Contenido de ejemplo')
        data = {'title': 'Nuevo Título', 'info': 'Nuevo contenido'}
        response = self.client.put(f'/api/posts/{post.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        post = Post.objects.create(userId=self.user, title='A Eliminar', info='Contenido a eliminar')
        response = self.client.delete(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
