from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'web/index.html', {})

def about(request):
    return render(request, 'web/about.html', {})

def contact(request):
    return render(request, 'web/contact.html', {})

def menu(request):
    return render(request, 'web/menu.html', {})

def service(request):
    return render(request, 'web/service.html', {})

def reservations(request):
    return render(request, 'web/reservations.html', {})

def testimonial(request):
    return render(request, 'web/testimonial.html', {})