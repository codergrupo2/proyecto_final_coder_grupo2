from django.db import models
from django.conf import  settings
from django.contrib.auth.models import User
from smbapp.fields import CaseInsensitiveCharField
from django.shortcuts import redirect, render



# Create your models here

#Modelo de intrumento
class Instrument (models.Model):
    name =  CaseInsensitiveCharField(max_length=100, unique=True, blank=False)
    def __str__(self):
        return self.nombre

#Modelo de musico
class Musician (models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.ManyToManyField (Instrument)
    def __str__(self):
        return self.email

#modelo de banda
class Band (models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    member = models.ManyToManyField(Musician)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) :
        return f"{self.title} + {self.creator}"

#modelo de post
class Post (models.Model):
    band = models.ForeignKey (Band, on_delete=models.CASCADE)
    instrument = models.ForeignKey (Instrument,on_delete=models.CASCADE)
    text = models.CharField(max_length=140)

    