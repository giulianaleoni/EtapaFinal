from django import forms
from .models import Post, Comentario,Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','subtitulo', 'texto','categoria', 'imagen']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields =['nombre']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

