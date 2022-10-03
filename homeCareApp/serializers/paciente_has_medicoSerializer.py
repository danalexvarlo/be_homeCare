from homeCareApp.models.paciente_has_medico import Paciente_has_medico
from rest_framework import serializers

class PacienteHasMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente_has_medico
        fields = ['id_paciente', 'id_familiar', 'id_persona', 'id_medico']