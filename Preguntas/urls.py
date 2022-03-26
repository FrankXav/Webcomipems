from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('plantilla/', plantilla),
    path('listmaterias/', MateriaList.as_view()),
    path('listpreguntas/', PreguntasList.as_view()),
    path('listopciones/', OpcionesList.as_view()),
    path('opciones/', PreguntasoList.as_view()),
    path('preguntas/', MateriaspList.as_view()),
]