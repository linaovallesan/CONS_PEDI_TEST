from dataclasses import dataclass
from typing import Optional

@dataclass
class Pedido:
    id_pedi: int
    esta_pedi: str
    
    def cerrar_pedido(self) -> None:
        self.esta_pedi = "cerrado"
    
    @classmethod
    def crear_desde_dict(cls, data: dict) -> 'Pedido':
        return cls(
            id_pedi=data.get('id_pedi'),
            esta_pedi=data.get('esta_pedi', 'abierto')
        )
