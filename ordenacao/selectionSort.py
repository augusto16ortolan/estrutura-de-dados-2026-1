def selection_sort(lista):
    tamanho_lista = len(lista)

    contador = 1

    for i in range(tamanho_lista):
        menor_index = i

        for j in range(i + 1, tamanho_lista):
            if lista[j] < lista[menor_index]:
                menor_index = j
        
        lista[i], lista[menor_index] = lista[menor_index], lista[i]
        print(f"Passo {contador}: {str(lista)}")
        contador += 1

    return lista

lista = [8, 3, 7, 1, 4]
lista_ordenada = selection_sort(lista)
print(lista_ordenada)


