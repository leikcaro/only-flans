from django import forms

from .models import Flan


class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ["flan_id", "nombre", "descripcion"]

