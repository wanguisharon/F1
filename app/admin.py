from django.contrib import admin

# Register your models here.
from .models import Team,  Driver,  Race

admin.site.register(Team) 
admin.site.register(Driver)
admin.site.register(Race)