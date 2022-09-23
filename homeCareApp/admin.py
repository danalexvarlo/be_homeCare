from django.contrib import admin
from .models.persona import Persona
from .models.paciente import Paciente
from .models.medico import Medico
from .models.enfermero import Enfermero
from .models.familiar import Familiar
from .models.paciente_has_medico import Paciente_has_medico
from .models.signosVitales import SignosVitales
from .models.historiaClinica import HistoriaClinica 

admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Enfermero)
admin.site.register(Familiar)
admin.site.register(Paciente_has_medico)
admin.site.register(SignosVitales)
admin.site.register(HistoriaClinica)