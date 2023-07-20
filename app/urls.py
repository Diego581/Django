from django.urls import path
from .views import main_page, login, register, post, newpost

app_name = 'nombreApp'
urlpatterns = [
    path('', main_page, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name= 'register'),
    path('post/<int:id>', post, name='post'),
    path('newpost/<int:userId>/<int:categoryId>', newpost, name='newpost'),
]