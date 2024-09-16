from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciosesion/', views.inicio_sesion, name='iniciosesion'),
    path('crearcuenta/', views.crear_cuenta, name='crearcuenta'),
    path('cerrarsesion/', views.cerrar_sesion, name='cerrarsesion'),
    path('home/', views.home, name='home'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('terminos/', views.terminos, name='terminos'),
    path('buscar/', views.buscar, name='buscar'),
    path('publicacion/crear/',views.addPublicacion, name='crearPublicacion'),
    path('perfil/', views.perfil, name='perfil')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    