from django import forms
from .models import Post, PerfilUsuario
from django.forms import ModelForm

class UserProfileForm(ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['nombre', 'biografia', 'fecha_nacimiento', 'foto_perfil', 'edad']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "descripcion", "importante", 'imagen']
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "importante": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"})
        }