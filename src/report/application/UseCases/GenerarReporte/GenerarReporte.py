from ....domain.entities.Report import Report
from ....domain.patterns.repository.IReportRepository import IReportRepository


class GenerarReporte:
    def __init__(self, report_repository: IReportRepository):
        self.__report_repository = report_repository

    def run(self, campos: dict) -> list[tuple]:
        return self.__report_repository.generar(campos)