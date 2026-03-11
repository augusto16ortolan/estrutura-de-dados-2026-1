class DNodo:

    def __init__(self, valor = None):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return str(self.valor)