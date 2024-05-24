from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime


def inscripcion(request):
    inscripcion= Inscripcion.objects.all()
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
            return redirect('/')

        # Convertir fecha_str a un objeto datetime
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            #fecha_db = fecha.strftime('%Y-%m-%d')  # Convertir a formato YYYY-MM-DD para guardar en la base de datos
        except ValueError:
            messages.error(request, 'Formato de fecha inválido.')
            return redirect('/')
        
        # Verificar que el alumno existe y los datos coinciden
        try:
            alumno = Alumno.objects.get(DNI=DNI, apellido=apellido, nombre=nombre)
        except Alumno.DoesNotExist:
            messages.error(request, 'El alumno no existe o los datos no coinciden.')
            return redirect('/')
        
        # Verificar que la materia existe
        try:
            materia = Materia.objects.get(nombre=materia_nombre)
        except Materia.DoesNotExist:
            messages.error(request, 'La materia no existe.')
            return redirect('/')

        # Verificar que existe un examen para la materia y la fecha dada
        try:
            examen = Examen.objects.get(materia=materia, fecha=fecha)
        except Examen.DoesNotExist:
            messages.error(request, 'No existe un examen para la materia y fecha proporcionadas.')
            return redirect('/')
        
     #   if datetime.now() > Examen.fecha_limite_inscripcion:
      #      messages.error(request, 'La fecha límite de inscripción ha pasado.')
       #     return render(request, 'inscripcion.html')

        # Verificar si ya existe una inscripción para este alumno y examen
        if Inscripcion.objects.filter(alumno=alumno, examen=examen).exists():
            messages.error(request, 'El alumno ya está inscrito en este examen.')
            return redirect('/')

        # Crear la inscripción
        inscripcion = Inscripcion.objects.create(alumno=alumno, examen=examen, fecha_inscripcion=fecha)
        inscripcion.save()
        messages.success(request, '¡Examen registrado!')
        return redirect('/')


def edicionInscripcion(request,id):
    inscripcion = Inscripcion.objects.get(id=id)
    return render(request, "editarInscripcion.html", {"inscripcion": inscripcion})


def editarInscripcion(request):
    if request.method == 'POST':
        # Extraer los datos del formulario enviado
        id= request.POST['inscripcion_id']
        DNI = request.POST['txtDNI']
        apellido = request.POST['txtApellido']
        nombre = request.POST['txtNombre']
        materia_nombre = request.POST['txtMateria']
        fecha_str = request.POST['dateFecha']
        
        
        if not all([DNI, apellido, nombre, materia_nombre, fecha_str]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('/')

        # Convertir fecha_str a un objeto datetime
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            #fecha_db = fecha.strftime('%Y-%m-%d')  # Convertir a formato YYYY-MM-DD para guardar en la base de datos
        except ValueError:
            messages.error(request, 'Formato de fecha inválido.')
            return redirect('/')
        
        # Verificar que el alumno existe y los datos coinciden
        try:
            alumno = Alumno.objects.get(DNI=DNI, apellido=apellido, nombre=nombre)
        except Alumno.DoesNotExist:
            messages.error(request, 'El alumno no existe o los datos no coinciden.')
            return redirect('/')
        
        # Verificar que la materia existe
        try:
            materia = Materia.objects.get(nombre=materia_nombre)
        except Materia.DoesNotExist:
            messages.error(request, 'La materia no existe.')
            return redirect('/')

        # Verificar que existe un examen para la materia y la fecha dada
        try:
            examen = Examen.objects.get(materia=materia, fecha=fecha)
        except Examen.DoesNotExist:
            messages.error(request, 'No existe un examen para la materia y fecha proporcionadas.')
            return redirect('/')
        
        try:
            inscripcion= Inscripcion.objects.get(id=id)
        except Inscripcion.DoesNotExist:
            messages.error(request, 'No existe una inscripcion previa para modificar.')
            return redirect('/')
        

        # Actualizar la inscripción
        inscripcion.alumno= alumno
        inscripcion.examen= examen 
        inscripcion.fecha_inscripcion=fecha
        inscripcion.save()
        
        messages.success(request, '¡Inscripcion actualizada!')
        return redirect('/')

def eliminarInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.delete()

    messages.success(request, '¡Inscripcion eliminada!')

    return redirect('/')
