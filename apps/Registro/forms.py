from django import forms
from .models import  Solicitud
from django.contrib.auth.models import User

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['usuario','pelicula','fotografia']


        labels ={
            'usuario':'Nombre usuario',
            'pelicula':'Nombre pelicula',
            'fotografia':'Agregar imagen'
        }

        widgets = {
            'usuarios': forms.TextInput(attrs={'class': 'form-control'}),
            'pelicula': forms.TextInput(attrs={'class': 'form-control'}),
        }
