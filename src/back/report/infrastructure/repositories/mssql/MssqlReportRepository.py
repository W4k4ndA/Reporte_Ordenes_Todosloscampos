from datetime import datetime

from ....domain.patterns.repository.IReportRepository import IReportRepository
from .DBconfig import DBconfig
from ....domain.entities.Report import Report

class MssqlReportRepository(IReportRepository):
    
    def __init__(self):
            
        # self.__connection_object = DBconfig(server, database, username, password) #uncomment to use DBconfig with parameters
        
        self.__connection_object_1 = DBconfig(server='GF-SRVDEV01\\PRUEBAS', database='ServicioTecnico', username='sa', password='ad min8888')
        self.__connection_object_2 = None # DBconfig(server='GFCM-SCS\\CYS', database='ServicioTecnico', username='sa', password='ad min8888')
    
    def generar(self, report: Report, fecha_desde: datetime, fecha_hasta: datetime) -> list[tuple]:

        self.__report = report

        query_params = {
            "str_fecha_desde" : fecha_desde,
            "str_fecha_hasta" : fecha_hasta
        }
                                
        query_begin ="Select "
        query_end = " from vw_OrdenServicio1 os left join vw_Ordenes_Repuestos re on os.CodOrden = re.CodOrden where fechaIngreso between :str_fecha_desde and :str_fecha_hasta "
        query_agrupation = "group by "
                
        
        query = self.__construct_query(query_begin, query_end, query_agrupation)
                      
        result = self.__connection_object_1.make_query(query, query_params)
        
        if self.__connection_object_2:
            result += self.__connection_object_2.make_query(query, query_params)
        
        return result
    
    
    def __construct_query(self, query_begin: str, query_end: str, query_agrupation: str) -> str:
       
        query_body = ""
        
        for key, value in self.__report.campos.val.items(): 
            query_body += f"{value}, " #value
            query_agrupation += f"{key}, " if key != 'CodOrden' else f"os.{key}, "
        
        if "Repuestos" in query_agrupation:
            query_agrupation = query_agrupation.replace("Repuestos", "")
            query_agrupation = query_agrupation[:-4]
        else:
            #quitar la ultima coma
            query_agrupation = query_agrupation[:-2]
        
        
        #quitar la ultima coma
        query_body = query_body[:-2]
        
        query = query_begin + query_body + query_end + query_agrupation        
        
        return query