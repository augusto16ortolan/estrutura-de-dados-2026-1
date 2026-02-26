from ContaBancaria import ContaBancaria

class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        self.numeroConta = 0
        
    def criar_conta(self, titular):
        # titular deve ser informado

        self.numeroConta += 1
        contaBancaria = ContaBancaria(titular, self.numeroConta)
        self.contas.append(contaBancaria)

    def recuperar_conta(self, numeroConta):
        for conta in self.contas:
            if conta.numero == numeroConta:
                return conta
            
        print(f"Conta nao encontrada pelo numero {numeroConta}")    

    def exibir_contas(self):
        for conta in self.contas:
            print(f"Conta {conta.numero}, saldo {conta.saldo}, titular {conta.titular}")