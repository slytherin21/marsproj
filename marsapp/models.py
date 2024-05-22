from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='team/')
    join = models.BooleanField(default=False)

class customuser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
 
class Profile(models.Model):
    user = models.OneToOneField(customuser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="default.jpg", upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

