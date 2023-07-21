
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm  # Asegúrate de crear este formulario
from .models import Post , Categoria
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/postindividual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()


def editarPost(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'texto': post.texto, 'categoria':post.categoria, 'imagen':post.imagen})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.titulo = form.cleaned_data['titulo']
            post.subtitulo = form.cleaned_data['subtitulo']
            post.texto = form.cleaned_data['texto']
            post.categoria = form.cleaned_data['categoria']
            post.imagen = form.cleaned_data['imagen']
            post.save()
            return redirect('apps.posts:postindividual', id=id)
    
    return render(request, 'posts/editarPost.html', {'form': form})

def index(request):
    categorias = Categoria.objects.all()
    post = Post.objects.order_by('-publicado')[:3]
    return render(request, 'index.html', {'categorias': categorias, 'post': post})

# *Metodo para obtener Todos Los Posts de Una Categoria Especifica


def requestCategoria(request, id):
    try:
        categoria = existe_categoria(id)
        posts = Post.objects.all().filter(categoria=id)
    except Exception:
        categoria = Categoria.objects.get(id=id)
        posts = Post.objects.all().filter(categoria=id)
    context = {
        'categoria': categoria,
        'posts': posts
    }
    return render(request, 'categoria/categoria.html', context)


def existe_categoria(id):
    for i in Categoria.objects.all:
        if i.id == id:
            return i
    return None

def agregarPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('apps.posts:posts')
    else:
        form = PostForm()
    return render(request, 'posts/crear.html', {'form': form})
