from django.urls import path, include
from rest_framework import routers
from .views import main_page, login_view, register_view, post, newpost, deletepost, deletecomment
from .views import PostViewSet, CommentViewSet, CreateUserView, CustomObtainAuthToken
from .views import CustomObtainAuthToken

#Urls de la api de post y comentarios
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

app_name = 'nombreApp'
urlpatterns = [
    path('', main_page, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('post/<int:id>', post, name='post'),
    path('newpost/', newpost, name='newpost'),
    path('post/deletepost/<int:id>', deletepost, name='deletepost'),
    path('post/deletecomment/<int:id>', deletecomment, name='deletecomment'),
    path('api/', include(router.urls)),  # Rutas de la API
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/login/', CustomObtainAuthToken.as_view(), name='login'),
]
