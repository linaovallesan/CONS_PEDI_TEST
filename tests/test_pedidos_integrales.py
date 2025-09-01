# Importaciones necesarias
import pytest
from django.test import Client
from django.urls import reverse

# Cliente de prueba de Django
client = Client()

# Clase para testear los pedidos integralmente
class TestPedidosIntegrales:

    # Test para verificar la respuesta exitosa de actualización de pedidos
    def test_actualizar_pedidos_exitoso(self):
        # URL correspondiente al endpoint 'test'
        url = reverse('test')

        # Simulación de la solicitud GET
        response = client.get(url)

        # Verificar el código de estado 200
        assert response.status_code == 200

        # Verificar que la respuesta contiene datos esperados (flujo de éxito)
        assert 'success' in response.json()['descripcion']
        
    # Test para verificar el manejo de errores al actualizar pedidos
    def test_actualizar_pedidos_error(self):
        # URL con parámetros incorrectos o falta de ellos (simulando error)
        url = reverse('test') + '?error_trigger=true'

        # Simulación de la solicitud GET
        response = client.get(url)

        # Verificar el manejo del error - debería ser un estado 400 o 500 según el diseño de la API
        assert response.status_code in [400, 500]

        # Verificar que la respuesta maneje los errores de forma adecuada
        assert 'error' in response.json()['descripcion']