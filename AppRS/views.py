"""Modulo para manejar las respuestas de las urls"""

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def crear_cuenta(request):
    return render(request, 'crearCuenta.html')

def inicio_sesion(request):
    return render(request, 'inicioSesion.html')

def cerrar_sesion(request):
    return render(request, 'cerrarSesion.html')

def posts(request):
    return render(request, 'Publicacion.html')


