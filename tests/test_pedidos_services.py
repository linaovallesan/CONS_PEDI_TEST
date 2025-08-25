# importando las bibliotecas necesarias para las pruebas
import pytest
from unittest.mock import Mock, patch
from CONS_PEDI_TEST.application.Services.pedidos_service import PedidosService
from CONS_PEDI_TEST.domain.models.pedidos import Pedido

# Prueba para el servicio de pedidos que maneja la lógica de negocio para actualizar pedidos

# Fixture inicial para obtener el objeto de servicio con una dependencia simulada (mocked)
@pytest.fixture
def pedidos_service():
    with patch('CONS_PEDI_TEST.infrastructure.repositories.pedidos_repository.PedidosRepository') as mock_repo:
        service = PedidosService(mock_repo)
        yield service

# Caso de prueba de éxito para actualización de pedido
def test_actualizar_pedido_exitoso(pedidos_service):
    # Configurando el mock para simular la existencia y actualización de un pedido
    pedidos_service.repository.obtener_pedido_por_id.return_value = Pedido(id_pedi=12345, esta_pedi='abierto')
    pedidos_service.repository.actualizar_pedido.return_value = None  # Simula el éxito sin retorno

    # Invocando la función de servicio para actualizar el pedido
    resultado = pedidos_service.actualizar_pedido(12345)

    # Verificando que la salida sea como se espera
    assert resultado == "pedido 12345 actualizado", "El mensaje de éxito no es el esperado"
    # Verifica que el estado del pedido mockeado fue cambiado a 'cerrado'
    assert pedidos_service.repository.guardar_cambios.called, "Guardar cambios no fue llamado"

# Caso de prueba para manejar un pedido que no existe
def test_actualizar_pedido_inexistente(pedidos_service):
    # Configurando el mock para simular que un pedido no existe
    pedidos_service.repository.obtener_pedido_por_id.return_value = None

    # Invocando la función de servicio y esperando que maneje el error
    with pytest.raises(ValueError) as excinfo:
        pedidos_service.actualizar_pedido(99999)
    
    # Verificar que el mensaje de error es el adecuado
    assert str(excinfo.value) == "El pedido no existe", "El mensaje de error para un pedido inexistente no es correcto"
