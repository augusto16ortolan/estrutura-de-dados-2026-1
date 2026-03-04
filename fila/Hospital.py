from Fila import Fila

class Hospital:

    def __init__(self):
        self._filaPrioridade = Fila()
        self._filaNormal = Fila()

    def retirar_ficha(self, nome, prioridade): # prioridade 0 ou 1, 1 vai para a fila de prioridade
        pass

    def atender(self): # lembrar da regra da prioridade
        pass

    def verificar_proximo_a_ser_atendido(self): # lembrar da regra da prioridade
        pass

    def imprimir_filas(self):
        pass