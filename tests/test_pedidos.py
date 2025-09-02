
# Importamos pytest y las clases o funciones necesarias para testear
import pytest
from CONS_PEDI_TEST.domain.models.pedidos import Pedido

# Creando los casos de prueba para la entidad Pedido

def test_crear_pedido():
    # Probando creación de un pedido con valores correctos
    pedido = Pedido(id_pedi=123, esta_pedi='abierto')
    
    # Comprobar que el pedido se crea con el estado correcto
    assert pedido.esta_pedi == 'abierto', "El estado del pedido debería ser 'abierto'"

def test_actualizar_estado_pedido():
    # Creando un objeto pedido y actualizando su estado
    pedido = Pedido(id_pedi=456, esta_pedi='abierto')
    pedido.esta_pedi = 'cerrado'

    # Comprobar que el estado del pedido se actualiza correctamente
    assert pedido.esta_pedi == 'cerrado', "El estado del pedido debería ser 'cerrado'"
    
def test_pedido_repr():
    # Creando un pedido y probando su representación en string
    pedido = Pedido(id_pedi=789, esta_pedi='en proceso')
    
    # Verificar que la representación str es correcta
    assert repr(pedido) == "<Pedido(id_pedi=789, esta_pedi='en proceso')>", "La representación del pedido no es correcta"
