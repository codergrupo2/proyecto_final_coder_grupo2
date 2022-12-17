from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from smbapp.views import *


urlpatterns = [
   
   path ( 'home/<int:page>', smbapp_home , name = 'smbapp-home'),
   path('', lambda req: redirect('home/1')),
   path ( 'actions/', smbapp_actions , name = 'smbapp-actions'),
   ####CRUD Users
   path ( 'register/', register, name = 'smbapp-register' ),
   path ( 'login/', login, name = 'smbapp-login' ),
   path ( 'profile/', smbapp_profile, name = 'smbapp-profile'),
   path ( 'profile/edit/', smbapp_edit_profile, name = 'smbapp-profile-edit'),
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
   path ( 'user/create/post', smbapp_add_post, name='create-post'),
   path ( 'band/delete/<id>/', delete_band, name='delete-band'),
   ##### CRUD Post
   path ( 'post/crud-posts/', crud_post, name='crud-posts'),
   path ( 'post/create/', smbapp_add_post, name='create-post'),
   path ( 'post/edit/<id>/', smbapp_edit_post, name='edit-post'),
   path ( 'post/delete/<id>/', smbapp_delete_post, name='delete-post'),
   path('about/', about_us_view, name='about-us'),
   path('messages/', ListThreads.as_view(), name='messages'),
   path('messages/create-thread/', CreateThread.as_view(), name='create-thread'),
   path('messages/<int:pk>/', ThreadView.as_view(), name="thread"),
   path('messages<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),

]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

