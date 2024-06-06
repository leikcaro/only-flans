from django import forms
from .models import Flan, Cliente, Contacto


# class FlanForm(forms.ModelForm):
#     class Meta:
#         model = Flan
#         fields = ["flan_id", "nombre", "descripcion"]
        


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellidos', 'email', 'asunto', 'mensaje']  # Excluir el campo 'edad'

