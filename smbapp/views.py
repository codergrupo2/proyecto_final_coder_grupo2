from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

#Import Auth Class
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as authlogin


#Import Vistas basadas en Clases
from proyecto_final_grupo2.settings import BASE_DIR
from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.views import View
#decorator
from django.contrib.auth.decorators import login_required

#import my models and forms
from smbapp.models import *
from smbapp.forms import *
from django.db.models import Q


# Create your views here w
def smbapp_home (request,page):
    posts = Post.objects.all()
    paginator = Paginator (posts, per_page = 2)
    page_post = paginator.get_page (page)
    return render (request, 'smbapp/index.html', {'page_post': page_post})


# Create your views here.
@login_required
def smbapp_actions (request):
    return render (request, 'smbapp/my_actions.html')

############ CRUD USER
#view to creat user
def register (request):
    if request.method == 'POST':

        form = FormCreateUser (request.POST)
        
        if form.is_valid():
            form.save()
            return render (request,'smbapp/index.html', {'mensaje':' User Created'})
    else:
        form = FormCreateUser()

    return render (request,'smbapp/register.html', {'form':form})

  
# Create your views here.
@login_required
def smbapp_profile (request):
    #I do it for obtain ID
    users=  User.objects.filter (username=request.user).values().all
    user_id = User.objects.get (username=request.user).pk

    try:
        users_extras = Musician.objects.get(user_id = user_id )
        return render (request, 'smbapp/my_profile.html', {'users': users, 'users_extras': users_extras})
    except:
        # Get avatar and Bio
        return render (request, 'smbapp/my_profile.html', {'users': users})

        
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

@login_required
def smbapp_edit_profile (request):
    user = request.user

    if request.method == 'POST':

            user_form = FormEditUser(request.POST)

            if user_form.is_valid():
                data = user_form.cleaned_data
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.email = data['email']
                user.save()
                return redirect('smbapp-profile')
    else:
        user_form = FormEditUser(initial ={'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email, 'username':user.username})

    return render(request, 'smbapp/edit_my_profile.html', {'user_form': user_form})

#Add bio and avatar
@login_required
def smbapp_add_musician (request):
 
    form = FormEditMusician()

    if request.method == "POST":

        form = FormEditMusician(request.POST, request.FILES)
        
        if form.is_valid():

            data = form.cleaned_data
            user = request.user
            user = Musician (user=request.user, bio_link =data["bio_link"], image=data["image"])
            user.save()
            return redirect("smbapp-profile")
    else:
        return render(request, "smbapp/add_my_musician.html", {"form": form})

    form = FormEditMusician()
    return render(request, "smbapp/add_my_musician.html", {"form": form})


#Add bio and avatar
@login_required
def smbapp_edit_musician (request):
 
    #I do it for obtain ID
    user_id = User.objects.get (username=request.user).pk
    # Get avatar and Bio
    users_extras = Musician.objects.get(user_id = user_id )

    if request.method == 'POST':

            user_form = FormEditMusician(request.POST, request.FILES)

            if user_form.is_valid():
                data = user_form.cleaned_data
                users_extras.bio_link = data['bio_link']
                if data['image'] is not None:
                    users_extras.image = data['image']
                users_extras.save()
                return redirect('smbapp-profile')
    else:
        users_form = FormEditMusician (initial ={ 'bio_link': users_extras.bio_link , 'image' : users_extras.image })
        return render(request, 'smbapp/edit_my_musician.html', {'users_form': users_form})


############ END CRUD USER


########### CRUD Bands ###############
## home crud bands
@login_required
def crud_bands (request):
    my_bands =  Band.objects.filter(creator=request.user)
    return render(request, "smbapp/crud_my_bands.html", {'my_bands': my_bands})

# Crear Banda
@login_required
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
            return redirect("/smbapp/actions")
        else:
            return render(request, "smbapp/create_band.html", {"form": formulario, "errors": formulario.errors })
    
    formulario = FormCreateBand()
    return render(request, "smbapp/create_band.html", {"form": formulario})

### edit band
@login_required
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
            band.save()
            return redirect("crud-bands")
        
        else:
            return render(request, "smbapp/edit_my_band.html", {"form": formulario, "errors": formulario.errors })
    
    formulario = FormCreateBand(initial={ "name" : band.name, "description": band.description })
    return render(request, "smbapp/edit_my_band.html", {"form": formulario})
     
### delete bands 
@login_required
def delete_band (request,id):
    band = Band.objects.get(id=id)
    band.delete()
    return redirect("crud-bands")

     

############END CRUD BANDS ######################


############# CRUD POST
@login_required
def crud_post (request):
    posts =  Post.objects.filter(creator=request.user)
    return render(request, "smbapp/crud_my_post.html", {'posts': posts})
    
@login_required
def smbapp_add_post (request):
 
    form = FormCreatePost()

    if request.method == "POST":

        form = FormCreatePost(request.POST, request.FILES)
        
        if form.is_valid():
            
            data = form.cleaned_data
            post = Post (
                band =data["band"], 
                tour_name =data["tour_name"],
                tour_dates =data["tour_dates"],
                creator = request.user,
                text = data["text"],
                image= data["image"]
                )
            post.save()

            return redirect("/smbapp/home/1")
    else:
         form = FormCreatePost()
         return render(request, "smbapp/create_post.html", {"form": form})
    
    return render(request, "smbapp/create_post.html", {"form": form})

@login_required
def smbapp_edit_post (request, id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":

        formulario = FormEditPost (request.POST)
       
        if formulario.is_valid():
            data = formulario.cleaned_data
            post.tour_name =data["tour_name"]
            post.tour_dates =data["tour_dates"]
            post.text = data["text"]
            post.save()
            return redirect("crud-posts")
        else:
            return render(request, "smbapp/edit_my_post.html", {"form": formulario, "errors": formulario.errors })
    
    formulario = FormEditPost(initial={ "band" : post.band, "tour_name": post.tour_name , "tour_dates": post.tour_dates, "creator": post.creator, "text": post.text })
    return render(request, "smbapp/edit_my_post.html", {"form": formulario})
     
@login_required
def smbapp_delete_post (request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("crud-posts")
   
#### About us 
def about_us_view(request):
    return render(request,'smbapp/about_us.html')

##### MESSAGING APP #####

#Thread List
class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user ) | Q(receiver=request.user) )

        context = { 'threads': threads}

        return render(request, 'smbapp/messages.html', context)

class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        
        context = {'form': form}

        return render (request, 'smbapp/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                
                thread = ThreadModel.objects.filters(user=request.user, receiver=receiver)[0]
                
                return redirect('thread', pk=thread.pk)
            
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
               
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]

                return redirect ('thread', pl=thread.pk)
            
            if form.is_valid():
                thread = ThreadModel(
                    user = request.user,
                    receiver=receiver
                    )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except:
            return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context ={
            'thread': thread,
            'form': form,
            'message_list': message_list
        }
        return render( request, 'smbapp/thread.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )
        message.save()
        return redirect('thread', pk=pk)

##### END MESSAGING APP #####