from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import uuid

# Create your models here.
class Cliente(models.Model):
    
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, default="cliente@cliente.cl") 
    edad= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)],default=18)
    asunto = models.CharField(max_length=200, default="")
    mensaje = models.TextField(max_length=1000, default="") 
    

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.email}"

class Flan(models.Model):
    flan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    nombre = models.CharField(max_length=64) #Nombre del flan ej. Flan de ...
    descripcion = models.TextField() #Regular o Light
    preparacion = models.TextField() 
    ingredientes = models.TextField()
    img_url = models.ImageField(upload_to='static/flans/') 
    slug = models.SlugField() #flan_de_...
    is_private = models.BooleanField() #Premium/No Premium
    
    def __str__(self):

        return f"El {self.nombre} {self.img_url} es {self.descripcion} "
    