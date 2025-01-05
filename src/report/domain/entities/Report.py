from ...domain.patterns.ValueObjects import ReportCampos

class Report:
    def __init__(self, campos: ReportCampos) -> None:
        self.campos = campos
    
    def __str__(self):
        return f"Reporte con campos: {self.campos.val.keys()}"
    
        