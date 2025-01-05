

class ReportCampos:
    def __init__(self, campos: dict) -> None:
        self.val = campos
        self.campos_validos = [
            'CodOrden',
            'CodCliente',
            'NomCliente',
            'Email',
            'CodModelo',
            'NombreModelo',
            'CodMarca',
            'NombreMarca',
            'Serial1Marca',
            'Serial1',
            'Serial2Marca',
            'Serial2',
            'Serial3Marca',
            'Serial3',
            'Serial4Marca',
            'Serial4',
            'Serial5Marca',
            'Serial5',
            'CodOperadora',
            'NombreOperadora',
            'NoLinea',
            'FechaCompra',
            'GarantiaFabricante',
            'GarantiaCS',
            'CodNivel',
            'NombreNivel',
            'LoginIngreso',
            'FechaIngreso',
            'FechaSalida',
            'LoginRevision',
            'LoginReparacion',
            'FechaReparacion',
            'CodEstado',
            'CodStatus',
            'NomStatus',
            'CodCentro',
            'NombreCentro',
            'GarantiaFabricanteTCS',
            'GarantiaCSTCS',
            'ObsTecnico',
            'LastCodStatus',
            'ObsCliente',
            'CodSintoma',
            'NombreSintoma',
            'OrdenExterna',
            'Entregado',
            'Reingreso',
            'CodTipoSintoma',
            'NombreTipoSintoma',
            'Condiciones',
            'CurrentCodCentro',
            'CurrentNombreCentro',
            'PrecioNivel',
            'CodSegmento',
            'NombreSegmento',
            'CodCondicion',
            'NombreCondicion',
            'CodSeccion',
            'NombreSeccion',
            'CodTipoSeccion',
            'NombreTipoSeccion',
            'Tlf',
            'ObsResumen',
            'CodNivelOp',
            'NombreNivelOp',
            'Intercambio',
            'TipoOrden',
            'StatusDOA',
            'FechaStatusDOA',
            'LoginStatusDOA',
            'FechaOE',
            'Reportado',
            'FechaReportado'
        ]
        
        self.validar_campos(self.val)
    
    
    def validar_campos(self, campos: dict = None):
        if not campos:
            raise ValueError("Debe proporcionar un diccionario de campos")
        campos_invalidos = [campo for campo in campos.keys() if campo not in self.campos_validos]
        if campos_invalidos:
            raise ValueError(f"Los siguientes campos son inválidos: {campos_invalidos}")