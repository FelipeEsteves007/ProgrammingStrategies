def soma_listas_com_contagem(lista_de_listas):
    soma_total = 0
    acessos = 0
    somas = 0

    for sublista in lista_de_listas:
        for elemento in sublista:
            acessos += 1           
            soma_total += elemento  
            somas += 1

    total_operacoes = acessos + somas
    num_listas = len(lista_de_listas)
    total_elementos = sum(len(sub) for sub in lista_de_listas)
    acessos_esperados = total_elementos
    somas_esperadas = total_elementos

    print(f"Lista de entrada: {lista_de_listas}")
    print(f"Soma total: {soma_total}")
    print(f"Número de acessos: {acessos}")
    print(f"Número de somas: {somas}")
    print(f"Total de operações: {total_operacoes}\n")
    print("Complexidade teórica:")
    print(f"- Número de listas: {num_listas}")
    print(f"- Total de elementos: {total_elementos}")
    print(f"- Acessos esperados: {acessos_esperados}")
    print(f"- Somas esperadas: {somas_esperadas}")


lista = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11, 12], [13, 14]]
soma_listas_com_contagem(lista)