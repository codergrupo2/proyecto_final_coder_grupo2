from django.db import models
from django.conf import  settings
from django.contrib.auth.models import User
from smbapp.fields import CaseInsensitiveCharField
from django.shortcuts import redirect, render



# Create your models here


#Modelo de musico
class Musician (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(User)
    avatar = models.ImageField()
    bio_link = models.URLField()
    def __str__(self):
        return self.user_id
    
    def get (self):
        return self.name, self.email

#modelo de banda
class Band (models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='members')
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name='creator')
    def __str__(self) :
        return f"{self.name}"



#modelo de post
class Post (models.Model):
    band = models.ForeignKey (Band, on_delete=models.CASCADE)
    tour_name = models.CharField (max_length=100)
    tour_dates = models.DateField()
    text = models.CharField(max_length=140)
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name='post_creator')
    image = models.ImageField(upload_to = "media/")

    