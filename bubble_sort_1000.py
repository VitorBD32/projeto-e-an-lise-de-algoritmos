import random
import time

# Tipo Abstrato de Dados para sequência de números
class Sequencia:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, index):
        return self.elementos[index]

    def __setitem__(self, index, valor):
        self.elementos[index] = valor

    def __str__(self):
        return str(self.elementos)

# Algoritmo Bubble Sort
def bubble_sort(sequencia):
    n = len(sequencia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sequencia[j] > sequencia[j + 1]:
                sequencia[j], sequencia[j + 1] = sequencia[j + 1], sequencia[j]

# Função para gerar sequência aleatória sem repetição
def gerar_sequencia_aleatoria(tamanho):
    return Sequencia(random.sample(range(1, tamanho + 1), tamanho))

# Teste do algoritmo com vetor de 1000 elementos
def main():
    tamanho = 1000

    # Gerar vetor desordenado
    sequencia = gerar_sequencia_aleatoria(tamanho)
    print(f"Vetor desordenado: {sequencia}")

    # Ordenar com Bubble Sort e medir o tempo
    inicio = time.time()
    bubble_sort(sequencia)
    fim = time.time()

    print(f"Vetor ordenado: {sequencia}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")

if __name__ == "__main__":
    main()
