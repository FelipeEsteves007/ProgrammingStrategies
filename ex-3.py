# Implemente uma função em Python chamada soma_pares(lista) que recebe uma lista de números inteiros e retorna a 
# soma de todos os números pares presentes na lista. 

def soma_pares (lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma 
            
print(soma_pares([10, 23, 45, 6, 8]))

