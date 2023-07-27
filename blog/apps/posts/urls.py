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
    path('posts/<int:post_id>/editar_comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('posts/<int:post_id>/eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
]

