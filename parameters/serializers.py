from rest_framework import serializers
from .models import Parameter

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter

        fields = ['id', 'name', 'values', 'created_at', 'updated_at']

        read_only_fields = ['id', 'created_at', 'updated_at']
