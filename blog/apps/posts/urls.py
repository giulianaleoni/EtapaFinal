from django.urls import path
from .views import PostListView, PostDetailView,index,requestCategoria, postUser,agregarCategoria
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('', index, name='index'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='postindividual'),
    path('misposts/', postUser, name='postUser'),
    path('categoria/<int:id>', requestCategoria, name='categoria'),
    path('posts/editarPost/<int:id>/', views.editarPost, name='editar'),
    path('post/crear/', views.agregarPost, name='agregar'),
    path('posts/eliminar/<int:id>/', views.eliminarPost, name='eliminar'),
    path('categoria/', agregarCategoria, name='creacategoria'),
]

