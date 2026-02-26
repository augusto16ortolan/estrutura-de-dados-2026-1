class Produto:

    def __init__(self, nome, valor, quantidade, marca):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.marca = marca

    def vender(self, quantidadeVendida):
        if self.quantidade >= quantidadeVendida:
            self.quantidade -= quantidadeVendida
            print("Venda efetuada")
            return

        print("Estoque insuficiente para essa venda")

        