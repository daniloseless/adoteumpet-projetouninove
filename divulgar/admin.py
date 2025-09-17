from django.contrib import admin
from divulgar.models import *

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'especie', 'raca', 'usuario', 'status']
    ordering = ('id',)

admin.site.register(Raca)
admin.site.register(Pet, PetAdmin)