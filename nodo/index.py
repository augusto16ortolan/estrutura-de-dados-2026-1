from Nodo import Nodo

nodo1 = Nodo("Augusto")
nodo2 = Nodo("Bruno")
nodo3 = Nodo("Carlos")
nodo4 = Nodo("Eduardo")
nodo5 = Nodo("Felipe")
nodo6 = Nodo("Gustavo")

nodo1.proximo = nodo2
nodo2.proximo = nodo3
nodo3.proximo = nodo4
nodo4.proximo = nodo5
nodo5.proximo = nodo6

atual = nodo1

while atual != None:
    print(atual)
    atual = atual.proximo

