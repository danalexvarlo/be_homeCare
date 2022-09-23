from django.db import models
from .persona import Persona

class Medico(models.Model):
    id_medico = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Persona, related_name = 'medico', on_delete = models.CASCADE)
    especialidad = models.CharField('Especialidad', max_length = 30)