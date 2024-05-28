from django.shortcuts import render
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