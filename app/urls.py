from django.urls import path
from .views import index, login, register,post

app_name = 'nombreApp'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name= 'register'),
    path('post/<int:id>', post, name='post'),
]