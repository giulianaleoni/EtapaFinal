from django.shortcuts import render
from .models import Post , Categoria
from django.views.generic import ListView, DetailView


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model= Post
    template_name = "posts/postindividual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()
    
def index (request):
    categorias = Categoria.objects.all()
    post = Post.objects.order_by('publicado')[:3]
    print(post)
    return render(request, 'index.html' ,{'categorias':categorias,'post':post})

#*Metodo para obtener Todos Los Posts de Una Categoria Especifica
def requestCategoria(request,id):
    try:
        categoria = existe_categoria(id)
        posts = Post.objects.all().filter(categoria = id)
    except Exception:
        categoria = Categoria.objects.get(id = id)
        posts = Post.objects.all().filter(categoria = id)
    context={
            'categoria':categoria,
            'posts':posts
        }
    return render(request,'categoria/categoria.html',context)

def existe_categoria(id):
    for i in Categoria.objects.all:
        if i.id == id:
            return i
    return None