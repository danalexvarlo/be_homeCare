from django.db import models
from .persona import Persona

class Enfermero(models.Model):
    id_enfermero = models.BigAutoField(primary_key = True)
    id_persona = models.ForeignKey(Persona, related_name = 'enfermero', on_delete = models.CASCADE)