from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PerfilUsuario(models.Model):
    nombre = models.OneToOneField(User,on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField()
    # def __str__(self):
    #      return self.nombre.User
    
    
class Post(models.Model):
    titulo = models.CharField(max_length=100,blank=True)
    descripcion = models.TextField(blank=True)
    importante = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    
    # relacionamos con el usuario | si en caso el usuario se borra, pues se borran sus tareas
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.user.username}"    
    
    