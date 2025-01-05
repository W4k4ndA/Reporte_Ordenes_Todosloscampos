from abc import ABC, abstractmethod
from ..ValueObjects.ReportCampos import ReportCampos

class IReportRepository(ABC):
    @abstractmethod
    def generar(self, campos: ReportCampos) -> list[tuple]:
        pass 
    
    