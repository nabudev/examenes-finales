from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime, date

def index(request):
    return render(request, 'index.html')

def inscripcion(request):
    inscripcion= Examen.objects.all()
    return render(request, "inscripcion.html", {"Inscripciones": inscripcion})

def registrarInscripcion(request):
    if request.method == 'POST':
        # Extraer los datos del formulario enviado
        DNI = request.POST['txtDNI']
        apellido = request.POST['txtApellido']
        nombre = request.POST['txtNombre']
        materia_nombre = request.POST['txtMateria']
        fecha_str = request.POST['dateFecha']
        
        # Validar que los campos no estén vacíos
        if not all([DNI, apellido, nombre, materia_nombre, fecha_str]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'inscripcion.html')

        # Convertir fecha_str a un objeto datetime
        try:
            fecha = datetime.strptime(fecha_str, '%dd/%mm/%YYYY').date()
            fecha_db = fecha.strptime('%Y-%m-%d')  # Convertir a formato YYYY-MM-DD para guardar en la base de datos
        except ValueError:
            messages.error(request, 'Formato de fecha inválido.')
            return render(request, 'inscripcion.html')
        
        # Verificar que el alumno existe y los datos coinciden
        try:
            alumno = Alumno.objects.get(DNI=DNI, apellido=apellido, nombre=nombre)
        except Alumno.DoesNotExist:
            messages.error(request, 'El alumno no existe o los datos no coinciden.')
            return render(request, 'inscripcion.html')
        
        # Verificar que la materia existe
        try:
            materia = Materia.objects.get(nombre=materia_nombre)
        except Materia.DoesNotExist:
            messages.error(request, 'La materia no existe.')
            return render(request, 'inscripcion.html')

        # Verificar que existe un examen para la materia y la fecha dada
        try:
            examen = Examen.objects.get(materia=materia, fecha=fecha_db)
        except Examen.DoesNotExist:
            messages.error(request, 'No existe un examen para la materia y fecha proporcionadas.')
            return render(request, 'inscripcion.html')
        
        if datetime.now() > examen.fecha_limite_inscripcion:
            messages.error(request, 'La fecha límite de inscripción ha pasado.')
            return render(request, 'inscripcion.html')

        # Verificar si ya existe una inscripción para este alumno y examen
        if Inscripcion.objects.filter(alumno=alumno, examen=examen).exists():
            messages.error(request, 'El alumno ya está inscrito en este examen.')
            return redirect('inscripcion.html')

        # Crear la inscripción
        inscripcion = Inscripcion(alumno=alumno, examen=examen, fecha_inscripcion=fecha_db)
        inscripcion.save()
        messages.success(request, '¡Examen registrado!')
        return redirect('inscripcion.html')



def edicionInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    return render(request, "editarInscripcion.html", {"Inscripcion": inscripcion})


def editarInscripcion(request, id, DNI):
    alumno = get_object_or_404(Alumno, DNI=DNI)
    examen = get_object_or_404(Examen, id=id)

    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.alumno = alumno
    inscripcion.examen = examen
    inscripcion.save()

    messages.success(request, '¡Inscripcion actualizada!')

    return redirect('inscripcion.html')


def eliminarInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.delete()

    messages.success(request, '¡Inscripcion eliminada!')

    return redirect('inscripcion.html')
