from django.shortcuts import render
from . import models
import uuid
# Create your views here.

def home(request):
    
    return render(request, 'home.html', {})

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

    todos_lanes = models.Flan.objects.all() 
    context = {'Flan':todos_flanes}

    return render(request,'flan.html',context=context)

def flan_detail(request, flan_id):
    try:
        flan_id = uuid.UUID(flan_id)
    except ValueError:
        return render(request, 'error.html', {'message': 'Introduce un UUID válido.'})

    flan = get_object_or_404(Flan, flan_id=flan_id)
    return render(request, 'flan_detail.html', {'flan': flan})