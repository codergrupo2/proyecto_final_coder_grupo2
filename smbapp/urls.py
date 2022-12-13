from django.urls import path
from django.contrib.auth.views import LogoutView
from smbapp.views import *


urlpatterns = [
   path ( 'home/', smbapp_home , name = 'smbapp-home'),
   path ( 'profile/', smbapp_profile , name = 'smbapp-profile'),
   path ( 'register/', register, name = 'smbapp-register' ),
   path ( 'login/', login, name = 'smbapp-login' ),
   path ( 'logout/', LogoutView.as_view(next_page='smbapp-home'), name = 'smbapp-logout'),
   path ( 'instrument/create/', CreateInstrument.as_view() , name = 'create-instrument'),
   #CRUD BAND
   ## Search
   path ( 'band/crud-bands/', crud_bands, name='crud-bands'),
   path ( 'band/list/', list_band, name='list-band'),
   path ( 'band/create/', create_band, name='create-band'),
   path ( 'band/edit/', edit_band, name='edit-band'),
   path ( 'band/delete/', delete_band, name='delete-band'),
   #####

   path ( 'musician/add-instruments/', add_my_instruments, name='add-my-instruments'),
   path ( 'user/create/post', CreatePost.as_view(), name='create-post')
]