from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import main_page, login, register, post, newpost, deletepost, UserViewSet, PostViewSet, CommentViewSet, CategoryViewSet

app_name = 'nombreApp'

# Creando el enrutador y registrando tus ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', main_page, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('post/<int:id>', post, name='post'),
    path('newpost/', newpost, name='newpost'),
    path('deletepost/<int:id>', deletepost, name='deletepost'),
    
    # Añade las URLs del enrutador DRF a tus urlpatterns
    path('api/', include(router.urls)),
]