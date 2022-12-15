from django.urls import path
from django.contrib.auth.views import LogoutView
from smbapp.views import *


urlpatterns = [
   path ( 'home/<int:page>', smbapp_home , name = 'smbapp-home'),
   path ( 'actions/', smbapp_actions , name = 'smbapp-actions'),
   ####CRUD Users
   path ( 'register/', register, name = 'smbapp-register' ),
   path ( 'login/', login, name = 'smbapp-login' ),
   path ( 'profile/', smbapp_profile, name = 'smbapp-profile'),
   path ( 'profile/edit/', smbapp_edit, name = 'smbapp-profile-edit'),
   path ( 'profile/add/musician', smbapp_add_musician, name = 'smbapp-profile-add-musician'),
   path ( 'profile/edit/musician', smbapp_edit_musician, name = 'smbapp-profile-edit-musician'),
   #add one to home page to return first page
   path ( 'logout/', LogoutView.as_view(next_page='/smbapp/home/1'), name = 'smbapp-logout'),
   #CRUD BAND
   ## Search
   path ( 'band/crud-bands/', crud_bands, name='crud-bands'),
   path ( 'band/create/', create_band, name='create-band'),
   path ( 'band/edit/<id>/', edit_band, name='edit-band'),
   path ( 'band/delete/', delete_band, name='delete-band'),
   #####

   path ( 'user/create/post', CreatePost.as_view(), name='create-post')
]