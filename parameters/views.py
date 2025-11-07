from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Parameter
from .serializers import ParameterSerializer

class ParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear y editar parámetros.
    """
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
    lookup_field = 'name' 

