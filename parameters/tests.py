from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Parameter

class ParameterAPITests(APITestCase):
    def test_create_parameter(self):
        """
        Asegura que podemos crear un nuevo parámetro.
        """
        url = reverse('parameter-list') # DRF nombra las rutas automáticamente
        data = {'name': 'testFeatureFlag', 'values': True}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(Parameter.objects.count(), 1)
        
        param = Parameter.objects.get()
        self.assertEqual(param.name, 'testFeatureFlag')
        self.assertEqual(param.values, True)