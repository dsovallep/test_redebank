from rest_framework import serializers
from .models import Parameter

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter

        fields = ['id', 'name', 'values', 'created_at', 'updated_at']

        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_values(self, value):
        # Aceptar únicamente tipos JSON: null, bool, int, float, str, list, dict
        allowed = (type(None), bool, int, float, str, list, dict)
        if not isinstance(value, allowed):
            raise serializers.ValidationError('values debe ser JSON válido (null, bool, number, string, array u object)')
        return value
