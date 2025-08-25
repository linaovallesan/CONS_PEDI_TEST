from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PedidoORM(Base):
    __tablename__ = 'pedidos'
    
    id_pedi = Column(Integer, primary_key=True)
    esta_pedi = Column(String(50), nullable=False)
