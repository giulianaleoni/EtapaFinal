from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm  # Asegúrate de crear este formulario
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

def editarPost(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'texto': post.texto, 'categoria':post.categoria, 'imagen':post.imagen})


    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.titulo = form.cleaned_data['titulo']
            post.subtitulo = form.cleaned_data['subtitulo']
            post.texto = form.cleaned_data['texto']
            post.categoria = form.cleaned_data['categoria']
            post.imagen = form.cleaned_data['imagen']
            post.save()
            return redirect('apps.posts:postindividual', id=id)

    return render(request, 'posts/editarPost.html', {'form': form})

def index (request):
    categorias = Categoria.objects.all()
    post = Post.objects.order_by('-publicado')[:3]
    return render(request, 'index.html' ,{'categorias':categorias,'post':post})