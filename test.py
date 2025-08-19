def pesquisa_binaria (lista,item):
    baixo = 0 #começa no indice zero
    alto = len(lista) - 1 #comeca no ultimo elemento 

    while baixo <= alto: # enqunato baixo for menor ou igual a alto
        meio = (baixo + alto) // 2 # pega o indice do meio 
        chute = lista[meio] # e chuta esse indice 
        if chute == item: # se for retorna o indice 
            return meio
        if chute > item: # se o chute for maior que o item passado
            alto = meio - 1 # o alto diminui um
        else:
            baixo = meio + 1 # se não for aumenta um 
    return None 

minha_lista = [1, 3, 5, 7,9]
print(pesquisa_binaria(minha_lista, 7))