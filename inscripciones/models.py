from django.db import models

class Carrera(models.Model):
    nombre=models.CharField(max_length=60)
    
    def __str__(self):
        return self.nombre
    
class CarreraAnio(models.Model):
    año= models.CharField(max_length=1)
    carrera= models.ForeignKey(Carrera, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.año} {self.carrera}'

class Alumno(models.Model):
    DNI= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=20)
    nombre= models.CharField(max_length=20)
    carrera= models.ForeignKey(CarreraAnio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.apellido+ " " + self.nombre
    
class Materia(models.Model):
    nombre=models.CharField(max_length=60)
    carrera= models.ForeignKey(CarreraAnio, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} : {self.carrera}'
    
class Examen(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateField()
    fecha_limite_inscripcion = models.DateField()
    
    def __str__(self):
        return f'{self.materia} + {self.fecha}'
    
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.alumno} + "Examen: " + {self.examen}'
    
