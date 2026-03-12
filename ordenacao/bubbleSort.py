"""
lista = [8, 3, 7, 1]

print(lista)

# swap (troca)
lista[0], lista[1] = lista[1], lista[0]

print(lista)
"""

# bubble_sort = compara vizinho por vizinho e faz troca
def bubble_sort(lista):
    if len(lista) == 0:
        return lista
    
    is_ordenado = False
    contador = 1

    while not is_ordenado:
        is_ordenado = True
        for i in range(0, len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                print(f"Passo {contador}: {str(lista)}")
                contador += 1
                is_ordenado = False
    
    return lista

lista = [8, 3, 7, 1, 4]

# [3, 8, 7, 1, 4]
# [3, 7, 8, 1, 4]
# [3, 7, 1, 8, 4]
# [3, 7, 1, 4, 8]
# [3, 1, 7, 4, 8]
# [3, 1, 4, 7, 8]
# [1, 3, 4, 7, 8]
# total de 7 passos para ordenar a lista

# lista_ordenada = bubble_sort(lista)
# print(lista_ordenada)
