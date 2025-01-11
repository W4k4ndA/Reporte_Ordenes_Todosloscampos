from datetime import datetime
from typing import List
import io

from pandas import DataFrame
import pandas as pd

from ....report.infrastructure.ServiceContainer import ServiceContainer

class StreamlitReportHandler:
    
    
    @staticmethod
    def get_data_report(fecha_inicio:datetime, fecha_final:datetime, campos_seleccionados:list[str]):
        
        
        
        campos_dict = {campo:campo for campo in campos_seleccionados}
        data = ServiceContainer.report.generar.run(campos_dict, fecha_inicio, fecha_final)
        df = pd.DataFrame(data, columns=campos_seleccionados)

        return df
    
    def get_excel_data_report(data: DataFrame):
        bytes_io = io.BytesIO()
        data.to_excel(bytes_io, index=False)
        
        return bytes_io