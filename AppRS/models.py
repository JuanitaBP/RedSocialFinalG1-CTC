from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PerfilUsuario(models.Model):
    biografia=models.TextField(blank=True,null=True)
    foto_perfil=models.ImageField(blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


