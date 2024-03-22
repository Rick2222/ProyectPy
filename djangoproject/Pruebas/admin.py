from django.contrib import admin
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUser
from .form import ElegirInlineFormset

class ElegirRespuestasInline(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.Maximo_respuestas
    min_num = ElegirRespuesta.min_respuestas
    formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [ElegirRespuestasInline]  
    list_display = ["texto",]
    search_fields = ["texto","preguntas__texto"]

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ["preguntas", "respuestas", "correcta", "Puntos_obtenidos"]
    class Meta: 
        model = PreguntasRespondidas    

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(PreguntasRespondidas)
admin.site.register(QuizUser)
