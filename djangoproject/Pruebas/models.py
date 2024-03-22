from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
user = settings.AUTH_USER_MODEL

# Create your models here.
class Pregunta(models.Model):
    Intentos = 1
    texto = models.TextField(verbose_name="Texto de la Pregunta")

    def __str__(self):
        return self.texto
    
class ElegirRespuesta(models.Model):

    min_respuestas =3
    Maximo_respuestas = 5

    pregunta = models.ForeignKey(Pregunta, related_name="preguntas", on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name="Respuesta correcta", default=False, null=False)
    texto = models.TextField(verbose_name="Texto de la respuesta")

    def __str__(self):
        return self.texto 
    
class QuizUser(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name="Puntaje total", default=0, decimal_places=2, max_digits =10)

class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name= "Respuesta correcta", default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name= "Puntaje obtenido", default=0, decimal_places= 2, max_digits=6)
