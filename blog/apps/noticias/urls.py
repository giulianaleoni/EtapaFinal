from django.urls import path
from .views import NoticiasListView, DetalleNoticiaView
from . import views

app_name = 'noticias'

urlpatterns = [
    path('noticias/', NoticiasListView.as_view(), name='noticias'),
    path('noticias/<int:pk>', DetalleNoticiaView.as_view(), name='detalle_noticia'),
]
