from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import filters
from rest_framework.response import Response
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from .models import *
from .serializers import *

def index(request):
    return render(request, 'index.html')

def plantilla(request):
    return render(request, 'preguntas.html')

class MateriaList(generics.ListAPIView):
    serializer_class = materiasSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

class PreguntasList(generics.ListAPIView):
    serializer_class = preguntasSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

class OpcionesList(generics.ListAPIView):
    serializer_class = opcionesSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

""" class PreguntaDetail(generics.RetrieveAPIView):
    serializer_class = preguntasSerializer
    
    def get_queryset(self):
        return self.get_queryset().Meta.model.objects """

class PreguntasoList(generics.ListAPIView):
    queryset = opciones.objects.all()
    serializer_class = opcionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pregunta_o']

class MateriaspList(generics.ListAPIView):
    queryset = preguntas.objects.all()
    serializer_class = preguntasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['materia_p']