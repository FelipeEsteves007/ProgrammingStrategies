import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3000)

def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

def medir_tempo(func, n, repeticoes=5):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.time()
        func(n)
        fim = time.time()
        tempos.append(fim - inicio)
    return sum(tempos) / repeticoes

valores_n = list(range(100, 1001, 100))

tempos_iterativos = []
tempos_recursivos = []

for n in valores_n:
    print(f"Calculando fatorial para n={n}")

    tempo_iter = medir_tempo(fatorial_iterativo, n)
    tempos_iterativos.append(tempo_iter)

    tempo_rec = medir_tempo(fatorial_recursivo, n)
    tempos_recursivos.append(tempo_rec)

plt.figure(figsize=(10, 6))
plt.plot(valores_n, tempos_iterativos, marker='o', label='Iterativo')
plt.plot(valores_n, tempos_recursivos, marker='s', label='Recursivo')

plt.title('Comparação de Desempenho: Fatorial Iterativo vs Recursivo')
plt.xlabel('Valor de n')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
