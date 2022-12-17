from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget

from smbapp.models import *



#Form Creat User
class FormCreateUser (UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField (label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username' , 'password1', 'password2']

#Edit Form
class FormEditUser (UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=False )
    password2 = forms.CharField (label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=False)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email' ]


#Edit musician
class FormEditMusician (forms.Form):
    bio_link = forms.URLField (max_length=100, widget=forms.URLInput(attrs={'class':'form-control'}))
    image = forms.ImageField(required=False)




#Form to create band
class FormCreateBand(forms.Form):
    name = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=150,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by('email'),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Band
        fields = ['name', 'description', 'members']


#Form create post
class FormCreatePost(forms.ModelForm):
    band = forms.ModelChoiceField(queryset=Band.objects.all().order_by('name'))
    tour_name = models.CharField (max_length=100)
    tour_dates = forms.DateField (widget=AdminDateWidget)
    text = forms.CharField(max_length=250)
    image = forms.ImageField()
    
    class Meta:
        model = Post
        fields =['band', 'tour_name', 'tour_dates', 'text', 'image']

#Form Edit post
class FormEditPost(forms.ModelForm):
    tour_name = models.CharField (max_length=100)
    tour_dates = forms.DateField (widget=AdminDateWidget)
    text = forms.CharField(max_length=250)

    class Meta:
        model = Post
        fields =[ 'tour_name', 'tour_dates', 'text']

#Form Thread
class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


#MessageForm
class MessageForm(forms.Form):
    message= forms.CharField(label='', max_length=1000)