from django.db import models
from django.utils import timezone
# Create your models here.



#Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo= models.models.CharField( max_length=50,null=False)
    subtitulo= models.models.CharField(max_length=100,null=False,blank=True)
    fecha= models.DateTimeField(auto_now_add=True)
    texto= models.TextField(null=False)
    activo= models.BooleanField(default=True)
    categoria= models.
    imagen= models.
    publicado= models.