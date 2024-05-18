from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('inscripcion/', views.inscripcion),
    path('registrarInscripcion/', views.registrarInscripcion, name='registrarInscripcion'),
    path('edicionInscripcion/', views.edicionInscripcion),
    path('editarInscripcion/', views.editarInscripcion),
    path('eliminarInscripcion/', views.eliminarInscripcion),
]