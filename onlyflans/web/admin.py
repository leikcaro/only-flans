from django.contrib import admin
from .models import Cliente, Flan
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'edad', 'asunto', 'mensaje')


@admin.register(Flan)# o admin.site.register(Flan) 
class FlanAdmin(admin.ModelAdmin):
    list_display = ('flan_id', 'nombre', 'descripcion', 'preparacion', 'ingredientes', 'img_url', 'slug', 'is_private' )
