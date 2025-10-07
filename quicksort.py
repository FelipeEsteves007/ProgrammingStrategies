def quicksort(lista, inicio, fim):
    if inicio < fim:
        p = particiona(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)

def particiona(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

numeros = [7, 3, 8, 1, 5, 2, 9]
quicksort(numeros, 0, len(numeros) - 1)
print("Lista ordenada:", numeros)
