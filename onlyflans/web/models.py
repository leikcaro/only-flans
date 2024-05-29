from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30) 
    edad= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)]) 
    

    def __str__(self):

        return f"Cliente {self.nombres} {self.apellidos} tiene {self.edad} "
