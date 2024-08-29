from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciosesion/', views.inicio_sesion, name='iniciosesion'),
    path('crearcuenta/', views.crear_cuenta, name='crearcuenta'),
    path('cerrarsesion/', views.cerrar_sesion, name='cerrarsesion'),
    path('home/', views.posts, name='home')
    
    
    # path("saludar/nombre=<str:estudiante>", views.saludar),
    # path("",views.prueba),
]