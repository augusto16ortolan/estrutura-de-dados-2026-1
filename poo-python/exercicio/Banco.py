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
            print(conta)

    def exibir_total_contas(self):
        print(f"O banco {self.nome} tem {len(self.contas)} conta(s)")

    def exibir_valor_total_contas(self):
        saldo_total = 0

        for conta in self.contas:
            saldo_total += conta.saldo

        print(f"O banco {self.nome} tem R$ {saldo_total} de valor acumulado entre contas")

    def transferir_valor_entre_contas(self, numeroContaOrigem, numeroContaDestino, valorTransferencia):
        # adicionar todas as validacoes possiveis
        
        contaOrigem = self.recuperar_conta(numeroContaOrigem)
        contaDestino = self.recuperar_conta(numeroContaDestino)

        contaOrigem.sacar(valorTransferencia)
        contaDestino.depositar(valorTransferencia)

