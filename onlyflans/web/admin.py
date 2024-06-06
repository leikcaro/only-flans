from django.contrib import admin
from .models import Cliente, Flan, Contacto
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombres', 'apellidos', 'edad')
    
@admin.register(Contacto)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombres', 'apellidos', 'asunto', 'mensaje')


@admin.register(Flan)# o admin.site.register(Flan) 
class FlanAdmin(admin.ModelAdmin):
    list_display = ('flan_id', 'nombre', 'descripcion', 'preparacion', 'ingredientes', 'img_url', 'slug', 'is_private' )
