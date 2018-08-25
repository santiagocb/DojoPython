from django.db import models

class Estudiante(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Curso(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    estudiante=models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    fechaCreacion=models.DateTimeField(auto_now_add=True)
    habilitado=models.BooleanField(default=True)
    descripcion=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.name)
