# Importaciones necesarias
import pytest
import requests

# URL base para las pruebas
BASE_URL = "https://gen-halcon.azzorti.co/undefined/cons_pedi/"

# Test para verificar la respuesta exitosa de la API
def test_consulta_pedidos_exito():
    # Simula una solicitud GET
    response = requests.get(BASE_URL)
    # Verifica que el estado de la respuesta es 200
    assert response.status_code == 200
    # Verifica que la respuesta no está vacía
    assert response.json() is not None

# Test para verificar el manejo de errores en la API
def test_consulta_pedidos_error():
    # Simula una solicitud GET incorrecta
    response = requests.get(BASE_URL, params={'invalid': 'data'})
    # Verifica que el estado de la respuesta es 400
    assert response.status_code == 400
    # Verifica que la respuesta especifica el tipo de error
    assert "error" in response.text.lower()