from CONS_PEDI_TEST.domain.models.pedidos import Pedido
from CONS_PEDI_TEST.domain.repositories.pedidos_repository import PedidosRepository
from CONS_PEDI_TEST.infrastructure.unit_of_work import UnitOfWork
from CONS_PEDI_TEST.application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO
from typing import Optional

class PedidosService:
    def __init__(self, pedidos_repository: PedidosRepository, uow: UnitOfWork):
        self.pedidos_repository = pedidos_repository
        self.uow = uow
    
    def actualizar_pedido_a_cerrado(self, input_dto: PedidoInputDTO) -> PedidoOutputDTO:
        try:
            id_pedi = int(input_dto.id_pedido)
            
            with self.uow:
                pedido = self.pedidos_repository.obtener_por_id(id_pedi)
                
                if not pedido:
                    raise ValueError(f"Pedido con ID {id_pedi} no encontrado")
                
                pedido.cerrar_pedido()
                self.pedidos_repository.actualizar(pedido)
                self.uow.commit()
                
                return PedidoOutputDTO(
                    status=f"pedido {id_pedi} actualizado"
                )
        
        except ValueError as e:
            raise ValueError(f"ID de pedido inválido: {str(e)}")
        except Exception as e:
            self.uow.rollback()
            raise Exception(f"Error al actualizar pedido: {str(e)}")
