from abc import ABC, abstractmethod
from typing import Optional
from CONS_PEDI_TEST.domain.models.pedidos import Pedido

class PedidosRepository(ABC):
    
    @abstractmethod
    def obtener_por_id(self, id_pedi: int) -> Optional[Pedido]:
        pass
    
    @abstractmethod
    def actualizar(self, pedido: Pedido) -> None:
        pass
