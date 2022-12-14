from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget

from smbapp.models import *



#Form Creat User
class FormCreateUser (UserCreationForm):
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1', 'password2']
        help_texts = {k:'' for k in fields}

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
    # band = forms.ModelChoiceField(queryset=Band.objects.all().order_by('name'))
    # tour_name = models.CharField (max_length=100)
    # tour_dates = forms.DateField (widget=AdminDateWidget)
    # text = forms.CharField(max_length=250)
    # image = forms.ImageField()
    
    class Meta:
        model = Post
        fields =['band', 'tour_name', 'tour_dates', 'text', 'image']
    
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(FormCreatePost, self).__init__(*args, **kwargs)
       self.fields['band'].queryset = Band.objects.filter(creator=user)