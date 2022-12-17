from django.db import models
from django.conf import  settings
from django.contrib.auth.models import User
from smbapp.fields import CaseInsensitiveCharField
from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here


#Modelo de musico
class Musician (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="avatares", null=True, blank=True)


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
    image = models.ImageField(upload_to = "posts",null=True, blank=True)

#modelo message thread
class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

#modelo message
class MessageModel(models.Model):
    thread = models.ForeignKey('Threadmodel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)