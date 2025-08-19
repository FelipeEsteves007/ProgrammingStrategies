# Implemente uma função em Python chamada encontrar_maior(lista) que recebe uma lista de números inteiros 
# e retorna o maior valor da lista. Certifique-se de que o algoritmo funcione corretamente para qualquer lista não vazia. Teste seu código com as seguintes entradas:

# Entrada 1: [3, 7, 2, 9, 4] → Saída esperada: 9

# Entrada 2: [-5, -1, -10, -3] → Saída esperada: -1

def encontrar_maior(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero 
    return maior

print(encontrar_maior([3, 7, 2, 9, 4] ))