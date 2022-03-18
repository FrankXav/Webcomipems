from django.db import models

# Create your models here.

class materias(models.Model):
    materia = models.CharField(max_length=50, blank=False,null=False)
    correctos_m = models.IntegerField(default=0)
    intentos_m = models.IntegerField(default=0)

    def __str__(self):
        return self.materia

class preguntas(models.Model):
    materia_p = models.ForeignKey(materias, on_delete=models.CASCADE, blank=False, null=False)
    pregunta = models.CharField(max_length=500, blank=False, null=False)
    correctos_p = models.IntegerField(default=0)
    intentos_p = models.IntegerField(default=0)

    def __str__(self):
        return self.pregunta

class opciones(models.Model):
    opcion = models.CharField(max_length=200,null=False,blank=False)
    pregunta_o = models.ForeignKey(preguntas, on_delete=models.CASCADE, blank=False, null=False)
    correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.opcion
        
