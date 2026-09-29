from rest_framework import serializers
from .models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ["id", "nombre", "cantidad", "estado", "resultado", "fecha", "eliminado"]
        read_only_fields = ["resultado", "fecha", "eliminado"]

    def validate_cantidad(self, valor):
        if valor < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa.")
        return valor