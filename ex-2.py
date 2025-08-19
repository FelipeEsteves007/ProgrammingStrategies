# Implemente uma função em Python chamada contar_vogais(texto) que recebe uma string como entrada 
# e retorna o número total de vogais (a, e, i, o, u) presentes na string. Considere tanto letras maiúsculas quanto minúsculas. 
# Certifique-se de que o algoritmo funcione corretamente para qualquer entrada, incluindo strings vazias.

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

print(contar_vogais("Algoritmos"))