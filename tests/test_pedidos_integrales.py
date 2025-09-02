import pytest
import requests

# URL base para las pruebas de integración
BASE_URL = "https://gen-halcon.azzorti.co/undefined"

# Test integral para verificar la funcionalidad de consultar pedidos exitosamente
def test_consultar_pedidos_exitoso():
    # Se hace una petición GET al endpoint correspondiente
    response = requests.get(f"{BASE_URL}/cons_pedi/")
    
    # Verificación de que la respuesta tiene un código de estado 200
    assert response.status_code == 200
    
    # Opcionalmente, verificar elementos específicos del contenido de la respuesta
    # Esto depende de lo que deba contener la respuesta en un caso exitoso
    # Por ejemplo: assert 'detalles_pedido' in response.json()

# Test integral para verificar la manipulación de errores al consultar pedidos
def test_consultar_pedidos_error():
    # Simulación de entrada errónea o condición que lleva a un error
    # En este ejemplo, se utilizará una URL incorrecta (simulando un error en el endpoint)
    response = requests.get(f"{BASE_URL}/cons_pedi_incorrecto/")
    
    # Verificación de que la respuesta tiene un código de estado 400 (malformed request)
    assert response.status_code == 400
    
    # Verificación de la respuesta de error adecuada
    # Por ejemplo: assert 'error' in response.json()