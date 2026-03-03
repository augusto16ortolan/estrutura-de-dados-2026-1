from Pilha import Pilha
from Historico import Historico

class Navegador:

    def __init__(self):
        self.paginasAnteriores = Pilha()
        self.paginasPosteriores = Pilha()
        self.paginaAtual = None
        self.historicoCompleto = []

    def navegar(self, pagina): # funcao para navegar para paginas
        # precisamos validar se a pagina é igual a pagina atual
        if pagina == self.paginaAtual:
            print("Já estamos nessa página")
            return
        
        #validamos se a pagina atual é nula, quer dizer que é a primeira navegacao
        if self.paginaAtual == None:
            self.paginaAtual = pagina
            self.historicoCompleto.append(Historico(pagina))
            return
        
        self.paginasAnteriores.push(self.paginaAtual)
        self.paginaAtual = pagina
        self.historicoCompleto.append(Historico(pagina))

    def voltar(self):
        if self.paginaAtual == None:
            print("Não há páginas para voltar")
            return
        
        if self.paginasAnteriores.is_empty():
            print("Não há páginas para voltar")
            return
        
        self.paginasPosteriores.push(self.paginaAtual)
        self.paginaAtual = self.paginasAnteriores.pop()
        self.historicoCompleto.append(Historico(self.paginaAtual))

    def avancar(self):
        if self.paginaAtual == None:
            print("Não há páginas para avançar")
            return
        
        if self.paginasPosteriores.is_empty():
            print("Não há páginas para avançar")
            return
        
        self.paginasAnteriores.push(self.paginaAtual)
        self.paginaAtual = self.paginasPosteriores.pop()
        self.historicoCompleto.append(Historico(self.paginaAtual))

    def visualizar_pagina_atual(self):
        if self.paginaAtual == None:
            print("Não teve navegações ainda")
            return

        print(self.paginaAtual)

    def visualizar_historico_completo(self):
        print("Histórico completo: ")
        for historico in self.historicoCompleto:
            print(historico)

    def visualizar_navegador(self):
        print(f"Página atual: {self.paginaAtual}")
        print("=================")
        print(f"Páginas anteriores: {self.paginasAnteriores}")
        print("=================")
        print(f"Páginas posteriores: {self.paginasPosteriores}")
        print("=================")
        print("Histórico completo: ")
        for historico in self.historicoCompleto:
            print(historico)
