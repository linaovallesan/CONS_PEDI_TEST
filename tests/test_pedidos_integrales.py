# Librerías internas de Django para correr los tests con Pytest
from django.test import TestCase, Client

# Definición de la clase de prueba integral
class TestPedidos(TestCase):

    # Constructor de la clase de pruebas
    def setUp(self):
        # Cliente HTTP para tests de Django
        self.client = Client()

    # Test para una consulta de pedidos exitosa
    def test_consulta_pedidos_exitosa(self):
        # Realiza una petición GET al endpoint específico
        response = self.client.get('https://gen-halcon.azzorti.co/undefined/test')

        # Verificar que el código de respuesta es 200 (éxito)
        self.assertEqual(response.status_code, 200)

        # Verificar contenido de la respuesta en caso necesario

    # Test para un caso de error al consultar pedidos
    # Por ejemplo, suponer un error controlado como endpoint no encontrado
    def test_consulta_pedidos_error(self):
        # Realiza una petición GET a un endpoint incorrecto
        response = self.client.get('https://gen-halcon.azzorti.co/undefined/error')

        # Verificar que el código de respuesta es de error, p.ej. 404
        self.assertEqual(response.status_code, 404)