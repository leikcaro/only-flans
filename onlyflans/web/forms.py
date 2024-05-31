from django import forms
import uuid


class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ["flan_id", "nombre", "descripcion"]

    def clean_flan_id(self):
        flan_id = self.cleaned_data["flan_id"]
        try:
            uuid.UUID(str(flan_id))
        except ValueError:
            raise forms.ValidationError("Introduce un UUID válido.")
        return flan_id
