from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre = models.OneToOneField(User,on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre.User
    
    
class Post(models.Model):
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_post = models.DateTimeField()
    
    
    