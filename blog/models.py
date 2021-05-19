from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PUser(models.Model):
    username = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    confirm_password = models.CharField(max_length=250)
    
    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(PUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
