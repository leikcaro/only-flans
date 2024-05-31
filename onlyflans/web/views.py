from django.shortcuts import render, get_object_or_404
from . import models
#from .models import Flan
import uuid

# Create your views here.

def home(request):
    flanes_publicos = models.Flan.objects.filter(is_private=False)
    context = {'flanes': flanes_publicos}
    return render(request, 'home.html', context=context)

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def service(request):
    return render(request, 'service.html', {})

def reservations(request):
    return render(request, 'reservations.html', {})

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

