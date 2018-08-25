from rest_framework import serializers
from .models import Estudiante
from .models import Curso


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields=('id','name', 'lastname')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields=('id','name','estudiante','fechaCreacion', 'habilitado', 'descripcion')
