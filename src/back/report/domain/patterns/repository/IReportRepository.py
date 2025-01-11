from abc import ABC, abstractmethod
from datetime import datetime

from ...entities.Report import Report

class IReportRepository(ABC):
    @abstractmethod
    def generar(self, campos: Report, fecha_desde: datetime, fecha_hasta: datetime) -> list[tuple]:
        pass 
    
    