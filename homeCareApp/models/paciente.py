from tkinter import CASCADE
from django.db import models
from .persona import Persona
from .medico import Medico

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Persona, related_name = 'paciente', on_delete = models.CASCADE)
    medico = models.ForeignKey(Medico, related_name = 'paciente', on_delete = models.CASCADE)
    direccion = models.CharField('Direccion', max_length = 50)