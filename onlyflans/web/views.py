from django.shortcuts import render, redirect
from . import models
from web.models import Flan, ContactForm
from .forms import ContactFormForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django_ratelimit.decorators import ratelimit
import logging
from django.http import HttpResponse

#from django.http import HttpResponseRedirect

# from .forms import ContactFormModelForm
# from .forms import CustomUserCreationForm
# from django.contrib.auth import authenticate
#from .models import ContactForm


# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'lista_flanes': flanes_publicos}) # Flanes publicos-Index

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    #request.session['name',] #capturar nombre de usuario
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'lista_flanes': flanes_privados}) # Obtener los flanes privados

def lista_clientes(request):
    todos_clientes = models.Cliente.objects.all() 
    context = {'clientes':todos_clientes}
    return render(request,'list.html',context=context)


def lista_flanes(request):

    todos_flanes = models.Flan.objects.all() 
    context = {'Flan':todos_flanes}
    return render(request,'flan.html',context=context)

#
def contact(request):
    #validar metodo post
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        #validar información correcta
        if form.is_valid():
            #guardado de la información en la base de datos
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # redirección del metodo
            #return HttpResponseRedirect('/success')
            return redirect('/success')

    else: 
        # redirección del metodo
        form = ContactFormForm()
    return render(request,'contact.html',{'form':form})

def success(request):
    return render(request, 'success.html') 

logger = logging.getLogger(__name__)

@ratelimit(key='ip', rate='3/m', method='POST', block=True)
def login_view(request):
    was_limited = getattr(request, 'limited', False)
    
    if was_limited:
        logger.warning('Rate limit exceeded for IP: %s', request.META['REMOTE_ADDR'])
        return render(request, 'login.html', {'form': LoginForm(), 'error': 'Too many login attempts. Please try again later.'})

    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('welcome')
            else:
                form.add_error(None, 'Credenciales inválidas')
                error = 'Credenciales inválidas'
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form, 'error': error})

def logged_out(request):
    return render(request, 'logged_out.html')

def ratelimit_exceeded(request, exception):
    return HttpResponse('Rate limit exceeded. Please try again later.', status=429)

@ratelimit(key='ip', rate='3/m', block=True)
def test_ratelimit(request):
    if getattr(request, 'limited', False):
        return HttpResponse('Rate limit exceeded', status=429)
    return HttpResponse('Rate limit not exceeded')

def ratelimit_exceeded(request, exception):
    return HttpResponse('Ha superado el numero de intentos de login, ingrese al sitio más tarde.', status=429)

def logged_out(request):
    return render(request, 'logged_out.html') 
