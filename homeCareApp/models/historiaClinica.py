from django.db import models
from .paciente import Paciente
from .familiar import Familiar
from .persona import Persona
from .medico import Medico 

class HistoriaClinica(models.Model):
    id_historia = models.BigAutoField(primary_key = True)
    id_paciente = models.ForeignKey(Paciente, related_name = 'historiaclinica', on_delete = models.CASCADE)
    id_familiar = models.ForeignKey(Familiar, related_name = 'historiaclinica', on_delete = models.CASCADE)
    id_persona = models.ForeignKey(Persona, related_name = 'historiaclinica', on_delete = models.CASCADE)
    id_medico = models.ForeignKey(Medico, related_name = 'historiaclinica', on_delete = models.CASCADE)
    fecha = models.DateField()
    motivoConsulta = models.CharField('Motivo Consulta', max_length = 60)
    enfermedades = models.CharField('Enfermedades', max_length = 60)
    antecedentes = models.CharField('Antecedentes', max_length = 60)
    diagnostico = models.CharField('Diagnostico', max_length = 60)
    sugerenciasCuidados = models.CharField('Sugerencias Cuidados', max_length = 60)