from homeCareApp.models.persona import Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'usuario', 'nombre', 'apellido', 'rol']