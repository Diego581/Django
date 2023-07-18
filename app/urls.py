from django.urls import path
from .views import index, login, register

app_name = 'nombreApp'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name= 'register'),

]