from django.db import models

class Carrera(models.Model):
    nombre=models.CharField(max_length=60)
    
class CarreraAnio(models.Model):
    año= models.CharField(max_length=1)
    carrera= models.ForeignKey(Carrera, on_delete=models.CASCADE)

class Alumno(models.Model):
    DNI= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=12)
    nombre= models.CharField(max_length=12)
    carrera= models.ForeignKey(CarreraAnio, on_delete=models.CASCADE)
    
class Materia(models.Model):
    nombre=models.CharField(max_length=60)
    carrera= models.ForeignKey(CarreraAnio, on_delete=models.CASCADE)
    
class Examen(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    fecha_limite_inscripcion = models.DateTimeField()
    
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    
