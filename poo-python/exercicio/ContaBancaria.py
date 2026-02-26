class ContaBancaria:

    def __init__(self, titular, numero):
        self.titular = titular
        self.saldo = 0.0
        self.numero = numero

    def depositar(self, valorDepositado):
        # valorDepositado nao pode ser igual a zero
        # valorDepositadi nao pode ser negativo
        self.saldo += valorDepositado

    def sacar(self, valorSacado):
        # valorSacado nao pode ser maior do que o saldo da conta
        # valorSacado nao pode ser igual a zero
        # valorSacado nao pode ser negativo
        self.saldo -= valorSacado

    def exibir_saldo(self):
        print(f"O saldo da conta {self.numero} é R$ {self.saldo}") # formatar saldo como monetário do Brasil