from django.contrib import admin
from .models import Cliente, Flan
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'edad')


# admin.site.register(Flan) o @admin.register(Flan)?
class FlanAdmin(admin.ModelAdmin):
    list_display = ('flan_id', 'nombre', 'descripción')
