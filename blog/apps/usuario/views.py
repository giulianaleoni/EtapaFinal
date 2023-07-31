from django.shortcuts import render
from .forms import RegistroUsuarioform
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login
from django.http import JsonResponse
# Create your views here.


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioform

    def form_valid(self, form):
        messages.success(
            self.request, 'Registro exitoso. Por favor inicia sesión.')
        form.save()
        next_url = self.request.GET.get('next')
        if next_url:
            self.request.session['next'] = next_url

        return redirect('apps.usuario:login')


class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get('next')
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, 'Inicio de sesión exitoso.')
            login(self.request, form.get_user())  # Autenticar al usuario
            next_url = self.request.GET.get('next') or reverse('apps.posts:index')
            return JsonResponse({'success': True, 'next_url': next_url})
        else:
            return JsonResponse({'success': False, 'message': 'Usuario o contraseña incorrectos.'})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'message': 'Usuario o contraseña incorrectos.'})

class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout exitoso')
        return redirect('apps.usuario:login')

    def get_next_page(self):
        return reverse('apps.usuario:login')


def acercaDe(request):
    return render(request, 'about.html')
