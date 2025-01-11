from types import SimpleNamespace

from .repositories.mssql.MssqlReportRepository import MssqlReportRepository
from ..application.UseCases.GenerarReporte.GenerarReporte import GenerarReporte

report_repository = MssqlReportRepository()

ServiceContainer = SimpleNamespace(
    report = SimpleNamespace(
        generar = GenerarReporte(report_repository)
    )
)