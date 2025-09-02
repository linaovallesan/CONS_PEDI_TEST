
import pytest
import requests

# URL base para las solicitudes a la API
BASE_URL = "https://gen-halcon.azzorti.co/undefined"

# Pruebas integrales para el endpoint de pedidos
class TestPedidosAPI:
    
    # Test de éxitos al obtener pedidos
    def test_consulta_pedidos_exito(self):
        response = requests.get(f"{BASE_URL}/cons_pedi/")
        assert response.status_code == 200
        assert type(response.json()) is list  # Asumiendo que la API devuelve una lista de pedidos
    
    # Test de manejo de error al obtener errores en las solicitudes de pedidos
    def test_consulta_pedidos_error(self):
        # Modificar el endpoint para simular un error como 404 o 400
        response = requests.get(f"{BASE_URL}/cons_pedi_error/")
        assert response.status_code == 400
        assert "error" in response.text

# La estructura propuesta se basa en realizar llamadas directas al servidor utilizando el framework de testing pytest, comprobando tanto los escenarios exitosos como los de error. Se utiliza la biblioteca `requests` para realizar llamadas HTTP.