from django.contrib import admin
from smbapp.models import *

# Register your models here.

admin.site.register(Instrument)
admin.site.register(MyInstruments)
admin.site.register(Band)
admin.site.register(Post)

