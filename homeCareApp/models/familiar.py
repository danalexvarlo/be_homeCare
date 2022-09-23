from django.db import models
from .persona import Persona

class Familiar(models.Model):
    id_familiar = models.BigAutoField(primary_key = True)
    id_persona = models.ForeignKey(Persona, related_name = 'familiar', on_delete = models.CASCADE)
    telefono = models.CharField('Telefono', max_length = 20)
    direccion = models.CharField('Direccion', max_length = 60)
    correo = models.CharField('Correo', max_length = 60)