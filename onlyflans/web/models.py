from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import uuid

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30) 
    edad= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)]) 
    

    def __str__(self):

        return f"Cliente {self.nombres} {self.apellidos} tiene {self.edad} "

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
    