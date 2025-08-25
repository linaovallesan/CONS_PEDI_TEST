from CONS_PEDI_TEST.domain.repositories.pedidos_repository import PedidosRepository
from CONS_PEDI_TEST.domain.models.pedidos import Pedido
from CONS_PEDI_TEST.infrastructure.sql_alchemy.mappings import PedidoORM
from typing import Optional

class SQLAlchemyPedidosRepository(PedidosRepository):
    def __init__(self, session):
        self.session = session
    
    def obtener_por_id(self, id_pedi: int) -> Optional[Pedido]:
        pedido_orm = self.session.query(PedidoORM).filter_by(id_pedi=id_pedi).first()
        if pedido_orm:
            return Pedido(
                id_pedi=pedido_orm.id_pedi,
                esta_pedi=pedido_orm.esta_pedi
            )
        return None
    
    def actualizar(self, pedido: Pedido) -> None {
        pedido_orm = self.session.query(PedidoORM).filter_by(id_pedi=pedido.id_pedi).first()
        if pedido_orm:
            pedido_orm.esta_pedi = pedido.esta_pedi
            self.session.add(pedido_orm)
