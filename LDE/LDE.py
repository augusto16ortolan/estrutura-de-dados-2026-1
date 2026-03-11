from DNodo import DNodo

class LDE:

    def __init__(self):
        self.header = DNodo()
        self.trailer = DNodo()
        self.quantidade_itens = 0

    def __inserir_primeiro(self, novo_nodo):
        self.header.proximo = novo_nodo
        self.trailer.anterior = novo_nodo
        novo_nodo.anterior = self.header
        novo_nodo.proximo = self.trailer
        self.quantidade_itens += 1

    def inserir_inicio(self, valor):
        novo_nodo = DNodo(valor)

        if (self.quantidade_itens == 0): # sendo o primeiro valor a ser adicionado na lista
            self.__inserir_primeiro(novo_nodo)
            return

        # a lista ja possui itens
        atual_primeiro = self.header.proximo
        atual_primeiro.anterior = novo_nodo
        novo_nodo.proximo = atual_primeiro
        novo_nodo.anterior = self.header
        self.header.proximo = novo_nodo
        self.quantidade_itens += 1

    def inserir_fim(self, valor):
        novo_nodo = DNodo(valor)

        if (self.quantidade_itens == 0): # sendo o primeiro valor a ser adicionado na lista
            self.__inserir_primeiro(valor)
            return
        
        # a lista ja possui itens
        atual_ultimo = self.trailer.anterior
        atual_ultimo.proximo = novo_nodo
        novo_nodo.anterior = atual_ultimo
        novo_nodo.proximo = self.trailer
        self.trailer.anterior = novo_nodo
        self.quantidade_itens += 1

    def __remover_unico(self):
        if self.quantidade_itens == 0:
            print("A lista está vazia")
            return
        
        if self.quantidade_itens == 1:
            dado_a_remover = self.header.proximo
            dado_a_remover.proximo = None
            dado_a_remover.anterior = None
            self.header.proximo = None
            self.trailer.anterior = None
            self.quantidade_itens -= 1
            return dado_a_remover

    def remover_inicio(self):
        if self.quantidade_itens <=1: # quando tem um ou nenhum dado na lista
            return self.__remover_unico()
        
        # quando tem mais de um dado na lista
        dado_a_remover = self.header.proximo
        novo_primeiro_dado = dado_a_remover.proximo
        dado_a_remover.proximo = None
        dado_a_remover.anterior = None
        self.header.proximo = novo_primeiro_dado
        novo_primeiro_dado.anterior = self.header
        self.quantidade_itens -= 1
        return dado_a_remover

    def remover_fim(self):
        if self.quantidade_itens <=1: # quando tem um ou nenhum dado na lista
            return self.__remover_unico()
        
        # quando tem mais de um dado na lista
        dado_a_remover = self.trailer.anterior
        novo_ultimo_dado = dado_a_remover.anterior
        dado_a_remover.proximo = None
        dado_a_remover.anterior = None
        self.trailer.anterior = novo_ultimo_dado
        novo_ultimo_dado.proximo = self.trailer
        self.quantidade_itens -= 1
        return dado_a_remover

    def remover_especifico(self, dado):
        if self.quantidade_itens == 0:
            print("A lista está vazia")
            return

        item = self.header.proximo

        while item != self.trailer:
            if item.valor == dado:
                dado_a_remover = item
                dado_anterior = dado_a_remover.anterior
                dado_proximo = dado_a_remover.proximo
                dado_a_remover.proximo = None
                dado_a_remover.anterior = None
                dado_anterior.proximo = dado_proximo
                dado_proximo.anterior = dado_anterior
                self.quantidade_itens -= 1
                return dado_a_remover
            
            item = item.proximo
            
        print("Valor não encontrado na lista")
        return

    def imprimir_lista(self):
        pass

    def imprimir_lado_a_lado(self):
        if self.quantidade_itens == 0:
            print("A lista está vazia")
            return

        item = self.header.proximo

        valor_a_imprimir = ""
        while item != self.trailer:
            if item == self.header.proximo:
                valor_a_imprimir = f"[HEADER] => [{item}]"
            else:
                valor_a_imprimir += f" => [{item}]"

            item = item.proximo

        valor_a_imprimir += " <= [TRAILER]"

        print(valor_a_imprimir)
