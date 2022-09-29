from homeCareApp.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Model:
        model = Familiar
        fields = ['id_familiar', 'id_persona', 'telefono', 'direccion', 'correo']