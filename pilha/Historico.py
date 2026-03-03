from datetime import datetime

class Historico:

    def __init__(self, pagina):
        self.pagina = pagina
        self.dataHora = datetime.now()

    def __str__(self):
        return str(f"Página: {self.pagina} - data e hora: {self.dataHora}")