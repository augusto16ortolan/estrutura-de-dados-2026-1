class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e tenho {self.altura} de altura")

    def fazer_aniversario(self):
        self.idade += 1

    def recuperar_data_nascimento(self):
        return 2026 - self.idade
        