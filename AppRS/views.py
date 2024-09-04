"""Modulo para manejar las respuestas de las urls"""

from django.shortcuts import render, redirect
from django.http import HttpResponse

#Estas importaciones proporcionan las funciones y clases necesarias para manejar
# la autenticación, renderización de plantillas y redirecciones en Django.
from django.contrib.auth.models import User # Modelo de usuario predeterminado de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    return render(request, 'index.html')

def crear_cuenta(request):
    form = UserCreationForm # Instancia del formulario
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password1"],
        )
        user.save()  # Guardar el usuario en la base de datos
        login(request, user)
        return redirect("home")
  
    return render(request, "crearCuenta.html", {"form": form})


#
def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirigir si el usuario ya está logueado
    
    if request.method == "GET":
        return render(request, "inicioSesion.html", {"form": AuthenticationForm})
    else:
        print(request.POST)
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "inicioSesion.html",
                {
                    "form": AuthenticationForm,
                    "error": "El nombre o la contraseña del usuario, es incorrecta",
                },
            )
        else:
            login(request, user)
            return redirect("home")

def cerrar_sesion(request):
    logout(request)
    return redirect("index")

def posts(request):
    return render(request, 'Publicacion.html')


def privacidad(request):
    return render(request, 'privacidad.html')

def terminos(request):
    return render(request, 'terminos.html')

def buscar(request):
    return render(request, 'buscar.html')

def home(request):
    return render(request, 'home.html')

def perfil(request):
    return render(request, 'perfil.html')

def addPublicacion(request):
   return render(request, 'Publicacion.html')
