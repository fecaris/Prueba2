from django.shortcuts import render, redirect
from .models import Solicitud
from .forms import PeliculaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




def menu(request):
    return render(request, 'Movie/menu.html',{})

# class UsuarioCreate(CreateView):
#     model = Usuario
#     form_class = UsuarioForm
#     template_name = 'Registro/usuario_form.html'
#     success_url = reverse_lazy("list_usuarios")

class RegistroUsuario(CreateView):
    model = Solicitud
    template_name = "Registro/registrar.html"
    form_class = PeliculaForm
    success_url = reverse_lazy('list_usuarios')


class UsuarioList(ListView):
    model = Solicitud
    template_name = 'Registro/list_usuarios.html'
    # paginate_by = 4

class UsuarioUpdate(UpdateView):
    model = Solicitud
    form_class = PeliculaForm
    template_name = 'Registro/usuario_form.html'
    success_url = reverse_lazy('list_usuarios')

class UsuarioDelete(DeleteView):
    model = Solicitud
    template_name = 'Registro/usuario_delete.html'
    success_url = reverse_lazy('list_usuarios')

