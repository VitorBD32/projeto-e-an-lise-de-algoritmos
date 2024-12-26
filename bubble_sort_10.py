import random
import time

# Algoritmo Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Gera um vetor de 10 elementos desordenados e sem repetição
def gerar_vetor_unico(tamanho):
    return random.sample(range(1, tamanho * 10), tamanho)

# Teste do algoritmo
def main():
    tamanho = 10
    vetor = gerar_vetor_unico(tamanho)
    print(f"Vetor original: {vetor}")

    inicio = time.time()
    bubble_sort(vetor)
    fim = time.time()

    print(f"Vetor ordenado: {vetor}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")

if __name__ == "__main__":
    main()
