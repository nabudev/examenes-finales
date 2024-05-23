from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscripcion),
    path('registrarInscripcion/', views.registrarInscripcion),
    path('edicionInscripcion/<int:DNI>', views.edicionInscripcion),
    path('editarInscripcion/<int:id>', views.editarInscripcion),
    path('eliminarInscripcion/<id>', views.eliminarInscripcion),
]