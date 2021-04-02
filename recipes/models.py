from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Recipe(models.Model):
    Name = models.CharField(max_length=25,blank=False)
    Ingredients = models.CharField(max_length=9999,blank=False)
    Directions = models.CharField(max_length=9999,blank=False)
    Posted_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='poster',default='')
    Created = models.DateTimeField(auto_now=True)