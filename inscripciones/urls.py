from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscripcion),
    path('registrarInscripcion/', views.registrarInscripcion),
    path('edicionInscripcion/<id>', views.edicionInscripcion),
    path('editarInscripcion/', views.editarInscripcion),
    path('eliminarInscripcion/<id>', views.eliminarInscripcion),
]