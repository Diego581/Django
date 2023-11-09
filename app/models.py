from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True,)
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=1250)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True,)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)  
    creation_date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.comment

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)  

    def __str__(self) -> str:
        return self.category_name