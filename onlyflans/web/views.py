from django.shortcuts import render, redirect
from . import models
#from .models import Flan
import uuid
from .forms import ContactoForm
# Create your views here.

def home(request):
    flanes_publicos = models.Flan.objects.filter(is_private=False)
    context = {'flanes': flanes_publicos}
    return render(request, 'home.html', context=context)

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def gracias(request):
    return render(request, 'gracias.html', {})

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')  # Redirige a una página de agradecimiento
    else:
        form = ContactoForm()
    return render(request, 'contact.html', {'form': form})

def menu(request):
    return render(request, 'menu.html', {})

def service(request):
    return render(request, 'service.html', {})

def reservations(request):
    flanes_privados = models.Flan.objects.filter(is_private=True)
    context = {'flanes': flanes_privados}
    return render(request, 'reservations.html', context=context)

def testimonial(request):
    return render(request, 'testimonial.html', {})


def lista_clientes(request):

    todos_clientes = models.Cliente.objects.all() 
    context = {'clientes':todos_clientes}

    return render(request,'list.html',context=context)


def lista_flanes(request):

    todos_flanes = models.Flan.objects.all() 
    context = {'Flan':todos_flanes}

    return render(request,'flan.html',context=context)

