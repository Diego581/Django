from django.urls import path

from .views import main_page, login, register, post, newpost, deletepost, PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, CategoryListCreateView, CategoryDetailView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'nombreApp'



urlpatterns = [
    path('', main_page, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('post/<int:id>', post, name='post'),
    path('newpost/', newpost, name='newpost'),
    path('deletepost/<int:id>', deletepost, name='deletepost'),
    path('register/', RegisterView, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
   
]