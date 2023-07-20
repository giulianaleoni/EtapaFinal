from django.contrib import admin
from .models import Noticia
# Register your models here.


@admin.register(Noticia)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'fecha_publicacion')
