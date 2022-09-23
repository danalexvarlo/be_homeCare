from django.db import models
from .paciente import Paciente
from .persona import Persona
from .familiar import Familiar

class SignosVitales(models.Model):
    id_signos = models.BigAutoField( primary_key = True)
    id_paciente = models.ForeignKey(Paciente, related_name = 'signosvitales', on_delete = models.CASCADE)
    id_familiar = models.ForeignKey(Familiar, related_name = 'signosvitales', on_delete = models.CASCADE)
    id_persona = models.ForeignKey(Persona, related_name = 'signosvitales', on_delete = models.CASCADE)
    oximetria = models.DecimalField('Oximetria', max_digits = 5)
    frecuenciaRespiratoria = models.IntegerField('Frecuencia Respiratoria')
    frecuenciaCardiaca = models.IntegerField('Frecuencia Cardiaca')
    temperatura = models.DecimalField('Temperatura', max_digits = 15)
    presionArterial = models.IntegerField('Presion Arterial')
    glicemia = models.DecimalField('Glicemia', max_digits = 15)
    fecha = models.DateField()
