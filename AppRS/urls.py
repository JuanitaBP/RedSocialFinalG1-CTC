from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciosesion/', views.inicio_sesion, name='iniciosesion'),
    path('crearcuenta/', views.crear_cuenta, name='crearcuenta'),
    path('cerrarsesion/', views.cerrar_sesion, name='cerrarsesion'),
    path('home/', views.posts, name='home'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('terminos/', views.terminos, name='terminos'),
    path('buscar/', views.buscar, name='buscar'),
    path('addPublicacion/',views.addPublicacion, name='addPublicacion'),
    path('perfil/', views.perfil, name='perfil'),
    
]