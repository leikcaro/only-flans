from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

#Formulario de Contacto--arreglar la vinculacion---REVISAR POR FAVOR
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {})
    else:
        form=ContactForm()
    return render(request, 'contact.html', {'form': form})

def menu(request):
    return render(request, 'menu.html', {})

