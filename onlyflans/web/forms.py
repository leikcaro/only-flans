from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from .models import ContactFormForm

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='email' )
    customer_name = forms.CharField(max_length=64, label='name' )
    message = forms.CharField(label='message' )
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=64, 
        label="Nombre", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})