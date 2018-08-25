
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from dojoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cursos/', views.CursoView.as_view()),
    url(r'^estudiantes/', views.EstudianteView.as_view())
]
