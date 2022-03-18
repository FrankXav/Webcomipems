from rest_framework import serializers

from .models import *

class materiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = '__all__'

class preguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = preguntas
        fields = '__all__'

class opcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = opciones
        fields = '__all__'