from django import forms
from .models import Post, Comentario,Categoria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder,Button,Field,HTML


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','subtitulo', 'texto','categoria', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal '
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            'titulo',
            'subtitulo',
            'texto',
            'categoria',
            'imagen',
            ButtonHolder(Submit('submit', 'Guardar cambios', css_class='btn btn-success btn-guardar-cambios')),
        )

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields =['nombre']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 6, 'style': 'width: 1200px;'}),  # Ajusta el ancho según tus necesidades
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'container'
        self.helper.layout = Layout(
            Field('texto'),
            ButtonHolder(
                Submit('submit', 'Guardar Cambios', css_class='btn btn-primary'),
                Button('cancel', 'Cancelar', css_class='btn btn-primary', onclick="window.history.back();"),
                css_class='mt-3 text-end'
            )
        )

        self.fields['texto'].label = ''
