
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

#Import Auth Class
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as authlogin


#Import Vistas basadas en Clases
from proyecto_final_grupo2.settings import BASE_DIR
from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator




#import my models and forms
from smbapp.models import *
from smbapp.forms import *

# Create your views here w
def smbapp_home (request,page):
    posts = Post.objects.all()
    paginator = Paginator (posts, per_page = 2)
    page_post = paginator.get_page (page)
    return render (request, 'smbapp/index.html', {'page_post': page_post})


# Create your views here.
def smbapp_actions (request):
    return render (request, 'smbapp/my_actions.html')

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
  
# Create your views here.
def smbapp_profile (request):
    profiles =  User.objects.filter(username=request.user).values('first_name', 'last_name','email','username')
    print (profiles)
    return render (request, 'smbapp/my_profile.html', {'profiles': profiles})

        
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
                 #add one to return first page
                return redirect ("/smbapp/home/1")
             else:
                return render (request, 'smbapp/login.html', {"form": form, "errors": "Credenciales invalidas"})
        else:
            return render (request, 'smbapp/login.html', {"form": form, "errors": form.errors})
    form = AuthenticationForm()
    return render (request, 'smbapp/login.html', {"form": form, "errors": errors})


########### CRUD Bands ###############
## home crud bands
def crud_bands (request):
    my_bands =  Band.objects.filter(creator=request.user)
    return render(request, "smbapp/crud_my_bands.html", {'my_bands': my_bands})

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
            #add one to return first page
            return redirect("/smbapp/home/1")
        else:
            return render(request, "smbapp/band_form.html", {"form": formulario, "errors": formulario.errors })
    formulario = FormCreateBand()

    return render(request, "smbapp/band_form.html", {"form": formulario})

### edit band
def edit_band (request, id):
    band = Band.objects.get(id=id)
    
    if request.method == "POST":

        formulario = FormCreateBand (request.POST)
       
        if formulario.is_valid():
            data = formulario.cleaned_data
            band.name = data["name"]
            band.description = data['description']
            band.members.clear()
            band.save()

            list_members = data['members']
            for member in list_members:
                band.members.add(member)    
                print (band.members)       
            band.save()
            return redirect("crud-bands")
        
        else:
            return render(request, "smbapp/edit_my_band.html", {"form": formulario, "errors": formulario.errors })
    
    formulario = FormCreateBand(initial={ "name" : band.name, "description": band.description })
    return render(request, "smbapp/edit_my_band.html", {"form": formulario})
     
### delete bands 
def delete_band (request):
    pass 

############END CRUD BANDS ######################

#### Views As a CLASS

class CreatePost (CreateView):
    model = Post
    form_class = FormCreatePost
    template_name = "smbapp/post_form.html"
    success_url = '/smbapp/home/1'

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
