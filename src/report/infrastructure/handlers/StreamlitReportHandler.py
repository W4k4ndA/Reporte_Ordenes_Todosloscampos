from datetime import datetime

from ....report.infrastructure.ServiceContainer import ServiceContainer

class StreamlitReportHandler:
    
    
    @staticmethod
    def get_report(fecha_inicio:datetime, fecha_final:datetime, campos_seleccionados:list[str]):
        
        
        
        campos_dict = {campo:campo for campo in campos_seleccionados}
        return ServiceContainer.report.generar.run(campos_dict, fecha_inicio, fecha_final)