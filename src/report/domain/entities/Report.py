

class Report:
    def __init__(self, campos: dict) -> None:
        self.campos = campos
    
    def __str__(self):
        return f"Reporte con campos: {self.campos}"
    
        