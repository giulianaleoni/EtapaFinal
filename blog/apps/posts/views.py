from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm  # Asegúrate de crear este formulario
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

def actualizar_noticia(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            form = PostForm(instance=post)
        return render(request, 'posts/post_form.html', {'form' : form})