from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    userId  = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=1250)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    postId  = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    postId  = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name
