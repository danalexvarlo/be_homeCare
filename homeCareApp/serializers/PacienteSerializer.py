from homeCareApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id_paciente', 'usuario', 'medico', 'direccion', 'telefono', 'latitud', 'longitud', 'id_familiar']