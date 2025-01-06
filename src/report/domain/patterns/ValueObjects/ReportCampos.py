

class ReportCampos:
    def __init__(self, campos: dict) -> None:
        self.val = campos
        self.campos_validos = [
            'CodOrden',
            'CodCliente',
            'NombreCliente',
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
            'NombreStatus',
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
        
        
        for key, value in campos.items():
            if key not in self.campos_validos:
                raise ValueError(f"El campo {key} no es valido")
            
            if key == "CodOrden":
                campos[f"{key}"] = f"os.{value}"
            #mapeo de valores 'case when' para la consulta de db.
            if key == "GarantiaFabricante":
                campos[f"{key}"] = "case when GarantiaFabricante = 1 then 'SI' else 'NO' end as 'Garantia Fabricante'"
            if key == "GarantiaCS":
                campos[f"{key}"] = "case when GarantiaCS=1 then 'SI' else 'NO' end as 'Garantia CS'"
            if key == "CodEstado":
                campos[f"{key}"] = "case when CodEstado=2 then 'CERRADA' else 'ABIERTA' end as Estado"
            if key == "GarantiaFabricanteTCS":
                campos[f"{key}"] = "case when GarantiaFabricanteTCS = 1 then 'SI' else 'NO' end as 'Garantia Fabricante TCS'"
            if key == "GarantiaCSTCS":
                campos[f"{key}"] = "case when GarantiaCSTCS = 1 then 'SI' else 'NO' end as 'Garantia CS TCS'"
            if key == "Entregado":
                campos[f"{key}"] = "case when Entregado = 0 then 'SIN ENTREGAR' else 'ENTREGADA' end as '¿Entregado?'"
            if key == "Reingreso":
                campos[f"{key}"] = "case when Reingreso = 1 then 'SI' else 'NO' end as Reingreso"
            if key == "StatusDOA":
                campos[f"{key}"] = "case when StatusDOA = 0 then 'SIN APROBACION' else 'APROBADA' end as 'Status DOA'"
            if key == "TipoOrden":
                campos[f"{key}"] = "case when TipoOrden = 1 then 'CLIENTE' when TipoOrden = 2 then 'DOA' when TipoOrden = 3 then 'SEEDSTOCK' end as 'Tipo Orden'"