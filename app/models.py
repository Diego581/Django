from django.db import models

# Create your models here.
 
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=1250)
    creation_date = models.DateField()

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    creation_date= models.DateField()

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)