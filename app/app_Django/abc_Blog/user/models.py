from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname=models.CharField(max_length=255)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")  
    photo=models.ImageField(upload_to='profile',blank=True, null=True)
    profession = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    birthday = models.DateField(null=True)
    twitter = models.URLField(max_length=50, null=True)
    linkedin = models.URLField(max_length=50, null=True)
    facebook = models.URLField(max_length=50, null=True)

    def __str__(self) :
        return self.user.username