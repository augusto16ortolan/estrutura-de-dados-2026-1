def insertion_sort(lista):
    contador = 1

    for i in range(1, len(lista)):
        for j in range(0, i):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                print(f"Passo {contador}: {str(lista)}")
                contador += 1
    
    return lista

lista = [8, 3, 7, 1, 4]
print(lista)
lista_ordenada = insertion_sort(lista)
print(lista_ordenada)