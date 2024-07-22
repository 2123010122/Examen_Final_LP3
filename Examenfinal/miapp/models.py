from django.db import models


# Create your models here.
class Personas(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    sexo = models.TextField()
    fecha_de_registro = models.BooleanField()
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    sexo = models.TextField()
    
