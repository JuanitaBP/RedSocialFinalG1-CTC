"""Modulo para manejar las respuestas de las urls"""

from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import PerfilUsuario, Post
from .forms import PostForm, UserProfileForm

#Estas importaciones proporcionan las funciones y clases necesarias para manejar
# la autenticación, renderización de plantillas y redirecciones en Django.
from django.contrib.auth.models import User # Modelo de usuario predeterminado de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirigir si el usuario ya está logueado
    return render(request, 'index.html')

def crear_cuenta(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirigir si el usuario ya está logueado

    form = UserCreationForm # Instancia del formulario
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save() # Guardar el usuario en la base de datos
                login(request, user) # Iniciar sesión automáticamente
                return redirect("home")
            except:
                return render(request, "crearCuenta.html", {"error": "El usuario ya existe"})
        else:
            return render(request, "crearCuenta.html", {"error": "Las contraseñas no coinciden"})
    return render(request, "crearCuenta.html",{"form": form})


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
    if request.user.is_authenticated:
        return render(request, "publicacion.html", {"data": "aquí se verán las tasks creadas"})
    return redirect("index")

def buscar(request):
    return render(request, 'buscar.html')

def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()  # Obtiene todas las tareas de la BD
        return render(request, "home.html", {"posts": posts})
    return redirect("index")

def perfil(request):
    # if not request.user.is_authenticated:
    #     # Redirige o muestra un mensaje si el usuario no ha iniciado sesión
    #     return redirect('inicioSesion.html')  # Suponiendo que tienes una vista de login
    # # Obtener el perfil del usuario autenticado
    # perfil = get_object_or_404(PerfilUsuario, user=request.user)
    # # Suponiendo que tienes un modelo Post para las publicaciones del usuario
    # #posts = Post.objects.filter(user=request.user)
    # # Pasar los datos del perfil y las publicaciones al template
    # context = {
    #     'perfil': perfil,
    #     'user': request.user,
    #     'posts': posts,
    # }
    
    
    # perfil = get_object_or_404(PerfilUsuario, nombre=request.user)
    # return render(request, 'perfil.html', {'perfil': perfil})
    
    
    # user = request.user
    # perfil = get_object_or_404(PerfilUsuario, nombre=user)

    # return render(request, "perfil.html", {"perfil": perfil})


    return render(request, "perfil.html")

def addPublicacion(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "Publicacion.html", {"form": PostForm})
        else:
            try:
                print(request.POST)
                form = PostForm(
                    request.POST, request.FILES
                )  # Crear el formulario con los datos enviados
                
                if form.is_valid():
                    nuevo_post = form.save(
                        commit=False
                    )  # Obtener los datos de ese form
                    nuevo_post.user = request.user
                    nuevo_post.save()
                    return redirect("home")
            except:
                return render(
                    request,
                    "Publicacion.html",
                    {"form": PostForm, "error": "No se pudo crear la publicación"},
                )

    redirect("login")

#    return render(request, 'Publicacion.html')
   
def privacidad(request):
    return render(request, 'privacidad.html')

def terminos(request):
    return render(request, 'terminos.html')
