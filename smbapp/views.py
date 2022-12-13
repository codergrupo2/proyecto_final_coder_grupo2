
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

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
    user = request.user
    print (user)
    if request.user.is_authenticated:
        my_bands = Band.objects.filter(creator=request.user)
        contex = {'my_bands': my_bands}
        return render (request, 'smbapp/index.html', contex)
    else:
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

# agrego mis instrumentos
def add_my_instruments (request):
    
    if request.method == "POST":
        formulario = FormAddMyInstruments(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user_id = request.user
            my_instruments = MyInstruments(user_id = user_id)
            my_instruments.save()

            list_instruments = data['instrument']
            for instrument in list_instruments:
                my_instruments.instruments.add(instrument)           
            my_instruments.save()

            return redirect("smbapp-home")
        else:
            return render(request, "smbapp/add_my_instruments.html", {"form": formulario, "errors": formulario.errors })
    formulario = FormAddMyInstruments()

    return render(request, "smbapp/add_my_instruments.html", {"form": formulario})

# Crear Banda
def create_band (request):
    
    if request.method == "POST":
        formulario = FormCreateBand(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            name = data['name']
            description = data['description']
            creator = request.user
             
            band = Band(name = name, description = description, creator=creator)
            band.save()

            list_members= data['members']
            for member in list_members:
                band.members.add(member)           
            band.save()

            return redirect("smbapp-home")
        else:
            return render(request, "smbapp/band_form.html", {"form": formulario, "errors": formulario.errors })
    formulario = FormCreateBand()

    return render(request, "smbapp/band_form.html", {"form": formulario})


#### Views As a CLASS
class CreateInstrument(CreateView):
     model = Instrument
     form_class = FormCreatInstrument
     template_name = "smbapp/instrument_form.html"
     success_url = '/smbapp/home/'


class CreatePost (CreateView):
    model = Post
    form_class = FormCreatePost
    template_name = "smbapp/post_form.html"
    success_url = '/smbapp/home/'

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs