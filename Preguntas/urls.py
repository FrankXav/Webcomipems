from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('listmaterias/', MateriaList.as_view()),
    path('listpreguntas/', PreguntasList.as_view()),
    path('listopciones/', OpcionesList.as_view())
]