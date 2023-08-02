from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen= models.ImageField(null=True,blank=True,upload_to='usuario',default='usuario/user-default.jpg')
    email = models.EmailField(unique= True, blank=False)
    es_colaborador = models.BooleanField(default=False)
    def __str__(self):
        return self.username