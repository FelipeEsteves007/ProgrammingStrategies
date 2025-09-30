import sys

# Aumenta o limite de recursão (opcional, para tentar evitar erro em listas grandes)
sys.setrecursionlimit(5000)

def insercao_recursiva(lista, n):
    # Caso base
    if n <= 1:
        return
    
    # Ordena os primeiros n-1 elementos recursivamente
    insercao_recursiva(lista, n-1)

    # Insere o último elemento na posição correta
    chave = lista[n-1]
    j = n - 2
    while j >= 0 and lista[j] > chave:
        lista[j+1] = lista[j]
        j -= 1
    lista[j+1] = chave


# Função para testar listas de diferentes tamanhos
def testar_listas():
    tamanhos = [50, 500, 1000, 1500, 2000, 2500, 3000]
    for tam in tamanhos:
        lista = list(range(tam-1, -1, -1))  # lista em ordem decrescente
        try:
            insercao_recursiva(lista, len(lista))
            print(f"Lista de tamanho {tam} ordenada com sucesso!")
        except RecursionError:
            print(f"⚠️ Erro de Recursão ocorreu com tamanho {tam}")
            break

testar_listas()
