from homeCareApp.models.enfermero import Enfermero
from rest_framework import serializers

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['id_enfermero', 'id_persona']