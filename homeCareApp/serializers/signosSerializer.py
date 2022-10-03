from msilib.schema import SelfReg
from homeCareApp.models.signosVitales import SignosVitales
from rest_framework import serializers

class signosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ['id_signos', 'id_paciente', 'id_familiar', 'id_persona', 'oximetria', 'frecuenciaRespiratoria', 'frecuenciaCardiaca', 'temperatura', 'presionArterial', 'glicemia', 'fecha']
    