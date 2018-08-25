from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Estudiante, Curso
from .serializers import EstudianteSerializer, CursoSerializer

# Create your views here.
class EstudianteView(generics.ListAPIView):
    serializer_class = EstudianteSerializer
    def get_queryset(self):
        queryset = Estudiante.objects.all()
        return queryset

    def post(self, request):
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


class CursoView(generics.ListAPIView):
    serializer_class = CursoSerializer
    def get_queryset(self):
            queryset = Curso.objects.all()
            return queryset


    def post(self, request):
        serializer=CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)
