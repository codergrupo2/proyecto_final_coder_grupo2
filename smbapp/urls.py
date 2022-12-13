from django.urls import path
from django.contrib.auth.views import LogoutView
from smbapp.views import *


urlpatterns = [
   path ( '', smbapp_home , name = 'smbapp-home'),
   path ( 'register/', register, name = 'smbapp-register' ),
   path ( 'login/', login, name = 'smbapp-login' ),
   path ( 'logout/', LogoutView.as_view(next_page='smbapp-home'), name = 'smbapp-logout'),
   path ( 'instrument/create/', CreateInstrument.as_view() , name = 'create-instrument'),
   path('band/create/', CreateBand.as_view(), name='create-band'),
   path('musician/create/', CreateMusician.as_view(), name='create-musician')
    
]