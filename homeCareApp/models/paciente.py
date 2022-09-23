from tkinter import CASCADE
from django.db import models
from .persona import Persona
from .medico import Medico
from .familiar import Familiar

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Persona, related_name = 'paciente', on_delete = models.CASCADE)
    medico = models.ForeignKey(Medico, related_name = 'paciente', on_delete = models.CASCADE)
    direccion = models.CharField('Direccion', max_length = 50)
    telefono = models.CharField('Telefono', max_length = 20)
    latitud = models.DecimalField('Latitud', max_digits = 10, decimal_places = 3)
    longitud = models.DecimalField('Longitud', max_digits = 10, decimal_places = 3)
    id_familiar = models.ForeignKey(Familiar, related_name = 'paciente', on_delete = models.CASCADE)