
from django.shortcuts import redirect, render
from django.http import HttpResponse

#Import Auth Class
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as authlogin


#Import Vistas basadas en Clases
from proyecto_final_grupo2.settings import BASE_DIR
import os
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

#Decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



#import my models and forms
from smbapp.models import *
from smbapp.forms import *

# Create your views here.
def smbapp_home (request):
    return render (request, 'smbapp/index.html')


#view to creat user
def register (request):
    
    if request.method == 'POST':

        form = FormCreateUser (request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request,'smbapp/index.html', {'mensaje':' User Created'})
    else:
        form = FormCreateUser()

    return render (request,'smbapp/register.html', {'form':form})
  

#view to login
def login (request):

    errors =''

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
             data = form.cleaned_data

             user = authenticate(username=data["username"], password=data["password"])             
             if user is not None:
                authlogin(request,user)
                return redirect ("smbapp-home")
             else:
                return render (request, 'smbapp/login.html', {"form": form, "errors": "Credenciales invalidas"})
        else:
            return render (request, 'smbapp/login.html', {"form": form, "errors": form.errors})
    form = AuthenticationForm()
    return render (request, 'smbapp/login.html', {"form": form, "errors": errors})


#### Views As a CLASS
class CreateInstrument(CreateView):
     model = Instrument
     form_class = FormCreatInstrument
     template_name = "smbapp/instrument_form.html"
     success_url = ''

class CreateBand(CreateView):
    model = Band
    form_class = FormCreateBand
    template_name= "smbapp/band_form.html"
    success_url = ''
    
class CreateMusician(CreateView):
    model = Musician
    form_class = FormCreateMusician
    template_name = "smbapp/musician_form.html"
    success_url = ''
    