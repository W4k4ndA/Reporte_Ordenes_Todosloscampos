from sqlalchemy import create_engine, text

from ....domain.patterns.repository.IReportRepository import IReportRepository
from ...Repositories.MSSQL.DBconfig import DBconfig
from ....domain.patterns.ValueObjects.ReportCampos import ReportCampos

class MSSQLReposiotry(IReportRepository):
    
    def __init__(self):
                
    #    self.__connection_object = DBconfig(server, database, username, password)
       self.__connection_object = DBconfig()
    
    def generar(self, campos: ReportCampos) -> list[tuple]:

        
        query_begin ="Select "
        query_body = ""
        query_end = " from vw_OrdenServicio1 os left join vw_Ordenes_Repuestos re on os.CodOrden = re.CodOrden"
        query_agrupation = ""
        
        
        for key in campos.val.keys():
            value = f"{key}, " 
            query_body += value
        
        #quitar la ultima coma
        query_body = query_body[:-2]
        
        query = query_begin + query_body + query_end + query_agrupation
        
        result = self.__connection_object.make_query(query)
        
        return result