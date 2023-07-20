from django.shortcuts import render
from .models import Noticia
from django.views.generic import ListView, DetailView
# Create your views here.


class NoticiasListView(ListView):
    model = Noticia
    template_name = "noticias/noticias.html"
    context_object_name = "noticias"
    ordering = "-fecha_publicacion"


class DetalleNoticiaView(DetailView):
    model = Noticia
    template_name = 'noticias/detalle_noticia.html'
    context_object_name = 'noticia'
