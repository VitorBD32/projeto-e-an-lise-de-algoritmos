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

# Gerar um vetor de 100 elementos desordenados e sem repetição
def gerar_vetor_desordenado_unico(tamanho):
    return Sequencia(random.sample(range(1, tamanho + 1), tamanho))

# Teste do algoritmo com medição de tempo
def main():
    tamanho = 100
    vetor = gerar_vetor_desordenado_unico(tamanho)

    print(f"Vetor antes da ordenação: {vetor}")

    inicio_tempo = time.time()
    bubble_sort(vetor)
    fim_tempo = time.time()

    print(f"Vetor após a ordenação: {vetor}")
    print(f"Tempo de execução da ordenação: {fim_tempo - inicio_tempo:.6f} segundos")

if __name__ == "__main__":
    main()
