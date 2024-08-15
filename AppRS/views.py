"""Modulo para manejar las respuestas de las urls"""

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Aquí se implementará la lógica para la vista inicial"""
    posts = [
        {
            "id": 1,
            "title": "Understanding Python Dictionaries",
            "content": "Dictionaries are powerful data structures in Python...",
            "author": "John Doe",
            "date": "2024-08-09",
            "likes": 0,
        },
        {
            "id": 2,
            "title": "Why Learn Python?",
            "content": "Python is a versatile language that can be used for web development...",
            "author": "Jane Smith",
            "date": "2024-08-08",
            "likes": 3,
        },
        {
            "id": 3,
            "title": "Advanced Python Techniques",
            "content": "Explore the more advanced features of Python, including generators...",
            "author": "Alice Johnson",
            "date": "2024-08-07",
            "likes": 20,
        },
    ]

    return render(request, "index.html", {"posts": posts, "program": "crack the code"})


# Utilizando ruta dinámica
def saludar(request, estudiante):
    message = f"Bienvenida {estudiante}"
    data = [1, 2, 3, 4]
    return HttpResponse(message)