from datetime import datetime

from ....domain.patterns.ValueObjects.ReportCampos import ReportCampos
from ....domain.entities.Report import Report
from ....domain.patterns.repository.IReportRepository import IReportRepository


class GenerarReporte:
    def __init__(self, report_repository: IReportRepository):
        self.__report_repository = report_repository

    def run(self, campos: dict, fecha_desde: datetime, fecha_hasta: datetime) -> list[tuple]:
        camps =  Report(ReportCampos(campos))
        return self.__report_repository.generar(camps, fecha_desde, fecha_hasta)