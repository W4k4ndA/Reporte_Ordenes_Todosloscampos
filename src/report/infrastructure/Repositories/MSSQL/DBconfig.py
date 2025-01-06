from sqlalchemy import create_engine, text


class DBconfig:
    def __init__(self: str = None, server:str = None, database:str=None, username:str=None, password:str=None):
                
        #Server Access Data
        self.__server = server or '127.0.0.1'
        self.__database = database or 'ServicioTecnico'
        self.__username = username or 'sa'
        self.__password = password or 'ad min8888'

        self.__make_connection()
        

    def __make_connection(self):
        connection_string = f'mssql+pyodbc://{self.__username}:{self.__password}@{self.__server}/{self.__database}?driver=ODBC+Driver+17+for+SQL+Server'
        self.__engine = create_engine(connection_string)

        connection = self.__engine.connect()

        self.__connection = connection

        return self.__connection
    
    def make_query(self, query, params: dict = None):
        query = text(query)
        parameters = params
        
        results = None
        if params is None :
                results = self.__connection.execute(query)
        else:
            if type(params) == dict :
                print("Ejecutamos la consulta CON parametros")        
                results = self.__connection.execute(query, parameters)
                
        
        return results.fetchall()