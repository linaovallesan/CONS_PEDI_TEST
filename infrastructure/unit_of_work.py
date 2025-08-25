from abc import ABC, abstractmethod
from CONS_PEDI_TEST.infrastructure.sql_alchemy.session_factory import SessionFactory

class UnitOfWork(ABC):
    
    @abstractmethod
    def __enter__(self):
        pass
    
    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    @abstractmethod
    def commit(self):
        pass
    
    @abstractmethod
    def rollback(self):
        pass

class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: SessionFactory):
        self.session_factory = session_factory
        self.session = None
    
    def __enter__(self):
        self.session = self.session_factory.get_session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        self.session.close()
    
    def commit(self):
        self.session.commit()
    
    def rollback(self):
        self.session.rollback()
