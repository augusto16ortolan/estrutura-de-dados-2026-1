from LDE import LDE

lista = LDE();
lista.inserir_inicio("Augusto")
lista.inserir_inicio("Bruno")
lista.inserir_fim("Carlos")
lista.inserir_fim("Daniel")
lista.inserir_fim("Eduardo")
lista.imprimir_lado_a_lado()
#lista.remover_inicio()
#lista.imprimir_lado_a_lado()
#lista.remover_fim()
#lista.imprimir_lado_a_lado()
lista.remover_especifico("Carlos 2")
lista.imprimir_lado_a_lado()
print(lista.quantidade_itens)