from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from smbapp.models import *



#Form to create instrument
class FormCreatInstrument (forms.ModelForm):
    name = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Instrument
        fields = ['name']

#Form Creat User
class FormCreateUser (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username' , 'password1', 'password2']
        help_texts = {k:'' for k in fields}

#Form to create band
class FormCreateBand(forms.Form):
    name = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=150,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all().order_by('email'),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Band
        fields = ['name', 'description', 'members']

#Form create musician - add my instruments
class FormAddMyInstruments(forms.Form):
    instrument = forms.ModelMultipleChoiceField(queryset=Instrument.objects.all().order_by('name'),widget=forms.CheckboxSelectMultiple)


#Form create post
class FormCreatePost(forms.ModelForm):
    band = forms.ModelChoiceField(queryset=Band.objects.all().order_by('name'))
    tour_dates = forms.DateField
    text = forms.CharField()
    
    class Meta:
        model = Post
        fields =['band', 'tour_dates', 'text']
    
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(FormCreatePost, self).__init__(*args, **kwargs)
       self.fields['band'].queryset = Band.objects.filter(creator=user)