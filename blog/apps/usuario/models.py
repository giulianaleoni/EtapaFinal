from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen= models.ImageField(null=True,blank=True,upload_to='usuario',default='usuario/user-default.jpg')

    es_colaborador = models.BooleanField(default=False)

    #def get_absolute_url(self):
    #    return reverse('index')

    def es_visitante(self):
        return not self.is_authenticated

    def es_miembro(self):
        return self.is_authenticated and not self.es_colaborador

    def puede_editar_post(self, post):
        return self.es_colaborador or self == post.usuario

    def puede_eliminar_post(self, post):
        return self.es_colaborador or self == post.usuario

    def __str__(self):
        return self.username