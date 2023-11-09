from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post, Comment

#Todos los test para la api

# Test de los comentarios
class CommentTests(APITestCase):
    #Setup (Genera un usuario para testing)
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(userId=self.user, title='Ejemplo', info='Contenido de ejemplo')

    # Create Comment (Genera un comentario y espera un status 201)
    def test_create_comment(self):
        data = {'postId': self.post.id, 'comment': 'Nuevo comentario'}
        response = self.client.post('/api/comments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Get Comment (Hace un get a los comentarios y espera un status 200)
    def test_get_comment(self):
        comment = Comment.objects.create(userId=self.user, postId=self.post, comment='Ejemplo de comentario')
        response = self.client.get(f'/api/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Update Comment (Hace un update al comentario creado antes y espera un status 200)
    def test_update_comment(self):
        comment = Comment.objects.create(userId=self.user, postId=self.post, comment='Comentario original')
        data = {'postId': self.post.id, 'comment': 'Comentario actualizado'}
        response = self.client.put(f'/api/comments/{comment.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete Comment (Hace un delete del comentario anterior y espera un status 204)
    def test_delete_comment(self):
        comment = Comment.objects.create(userId=self.user, postId=self.post, comment='Comentario a eliminar')
        response = self.client.delete(f'/api/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# Test de los Posteos
class PostTests(APITestCase):
    #Setup (Genera un usuario para testing)
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    # Create Post (Genera un comentario y espera un status 201)
    def test_create_post(self):
        data = {'title': 'Nuevo Post', 'info': 'Contenido del nuevo post'}
        response = self.client.post('/api/posts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # Get Post (Hace un get y espera un status 200)
    def test_get_post(self):
        post = Post.objects.create(userId=self.user, title='Ejemplo', info='Contenido de ejemplo')
        response = self.client.get(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    # Update Post (Hace un update del post anterior y espera un status 200)
    def test_update_post(self):
        post = Post.objects.create(userId=self.user, title='Ejemplo', info='Contenido de ejemplo')
        data = {'title': 'Nuevo Título', 'info': 'Nuevo contenido'}
        response = self.client.put(f'/api/posts/{post.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    # Delete Post (Hace un delete del post creado y espera un status 204)
    def test_delete_post(self):
        post = Post.objects.create(userId=self.user, title='A Eliminar', info='Contenido a eliminar')
        response = self.client.delete(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
