from django.contrib import admin
from smbapp.models import *

# Register your models here.
admin.site.register(Musician)
admin.site.register(Band)
admin.site.register(Post)

# @admin.register(Musician)
# class MusicianAdmin(admin.ModelAdmin):
#     list_display = ('user_id','email')