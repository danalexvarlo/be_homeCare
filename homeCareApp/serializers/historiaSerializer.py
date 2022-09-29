from homeCareApp.models.historiaClinica import HistoriaClinica
from rest_framework import serializers

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['id_historia', 'id_paciente', 'id_familiar', 'id_persona', 'id_medico', 'fecha', 'motivoConsulta', 'enfermedades', 'antecedentes', 'diagnostico', 'sugerenciasCuidados']