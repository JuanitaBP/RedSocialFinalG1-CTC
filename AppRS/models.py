from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

# Create your models here.
class PerfilUsuario(models.Model):
    nombre = models.OneToOneField(User,on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True,blank=True)
    seguidores = models.ManyToManyField(User, related_name='seguidores', blank=True)
    seguidos = models.ManyToManyField(User, related_name='seguidos', blank=True)
    posts_guardados = models.ManyToManyField('Post', related_name='guardado_por', blank=True)

    def __str__(self):
        return self.user.username

    # Método para contar los seguidores
    def num_seguidores(self):
        return self.seguidores.count()

    # Método para contar los seguidos
    def num_seguidos(self):
        return self.seguidos.count()

    def seguir(self, usuario):
        """El usuario actual sigue a otro usuario"""
        self.seguidos.add(usuario)

    def dejar_de_seguir(self, usuario):
        """El usuario actual deja de seguir a otro usuario"""
        self.seguidos.remove(usuario)

    def es_seguidor(self, usuario):
        """Verifica si el usuario actual está siguiendo a otro usuario"""
        return self.seguidos.filter(id=usuario.id).exists()

    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    importante = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    # relacionamos con el usuario | si en caso el usuario se borra, pues se borran sus tareas
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.titulo} - {self.user.username}"
    

    def dar_like(self, usuario):
        """Permite a un usuario darle like a la publicación"""
        self.likes.add(usuario)

    def quitar_like(self, usuario):
        """Permite a un usuario quitarle el like a la publicación"""
        self.likes.remove(usuario)

    def num_likes(self):
        """Cuenta el número de likes que tiene la publicación"""
        return self.likes.count()

    def es_likeado_por(self, usuario):
        """Verifica si un usuario ya le dio like a la publicación"""
        return self.likes.filter(id=usuario.id).exists()
    
