from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *

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