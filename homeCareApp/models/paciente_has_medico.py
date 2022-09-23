from django.db import models
from .familiar import Familiar
from .medico import Medico
from .paciente import Paciente
from .persona import Persona

class Paciente_has_medico(models.Model):
    id_paciente = models.ForeignKey(Paciente, related_name = 'paciente_has_medico', on_delete = models.CASCADE)
    id_familiar = models.ForeignKey(Familiar, related_name = 'paciente_has_medico', on_delete = models.CASCADE)
    id_persona = models.ForeignKey(Persona, related_name = 'persona_has_medico', on_delete = models.CASCADE)
    id_medico = models.ForeignKey(Medico, related_name = 'personas_has_medico', on_delete = models.CASCADE)