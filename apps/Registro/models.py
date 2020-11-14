from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Solicitud(models.Model):
    usuario = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    pelicula = models.CharField(max_length=30, null=False)
    fotografia = models.ImageField(upload_to='peliculas')

    def __str__(self):
        return str(self.fotografia)
