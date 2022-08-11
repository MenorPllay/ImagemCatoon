from django.contrib import admin
from .models import *

# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')


# admin.site.register(cartoonImg)
@admin.register(cartoonImg)
class Cartoo(admin.ModelAdmin):
    # list_display= (
    #     '__str__'
    # )
    
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
            'admindeleteimgs.js',
            )