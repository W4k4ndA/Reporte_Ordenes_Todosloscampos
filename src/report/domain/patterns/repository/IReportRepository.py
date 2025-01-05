from abc import ABC, abstractmethod


class IReportRepository(ABC):
    @abstractmethod
    def generar(self, campos: dict) -> list[tuple]:
        pass 
    
    