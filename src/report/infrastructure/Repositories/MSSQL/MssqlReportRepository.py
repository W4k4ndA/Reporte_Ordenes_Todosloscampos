from datetime import datetime

from ....domain.patterns.repository.IReportRepository import IReportRepository
from .DBconfig import DBconfig
from ....domain.entities.Report import Report

class MssqlReportRepository(IReportRepository):
    
    def __init__(self):
                
        # self.__connection_object = DBconfig(server, database, username, password) #uncomment to use DBconfig with parameters
        self.__connection_object = DBconfig()
    
    def generar(self, report: Report, fecha_desde: datetime, fecha_hasta: datetime) -> list[tuple]:

        query_params = {
            "str_fecha_desde" : fecha_desde,
            "str_fecha_hasta" : fecha_hasta
        }
                
        query_begin ="Select top 200 "
        query_body = ""
        query_end = " from vw_OrdenServicio1 os left join vw_Ordenes_Repuestos re on os.CodOrden = re.CodOrden where fechaIngreso between :str_fecha_desde and :str_fecha_hasta "
        query_agrupation = "group by "
        
        
        for key, value in report.campos.val.items(): 
            query_body += f"{value}, " #value
            query_agrupation += f"{key}, " if key != 'CodOrden' else f"os.{key}, "
        
        #quitar la ultima coma
        query_body = query_body[:-2]
        
        #quitar la ultima coma
        query_agrupation = query_agrupation[:-2]
        
        query = query_begin + query_body + query_end + query_agrupation        
                      
        result = self.__connection_object.make_query(query, query_params)
        
        return result