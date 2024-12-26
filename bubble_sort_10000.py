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

# Função para gerar um vetor aleatório sem repetição
def gerar_sequencia_aleatoria_sem_repeticao(tamanho):
    return Sequencia(random.sample(range(1, tamanho + 1), tamanho))

# Teste do algoritmo
def main():
    tamanho = 10000
    print(f"\nGerando vetor de {tamanho} elementos desordenados e sem repetição...")
    sequencia = gerar_sequencia_aleatoria_sem_repeticao(tamanho)
    print("Vetor desordenado:")
    print(sequencia)

    print("Iniciando a ordenação com Bubble Sort...")
    inicio = time.time()
    bubble_sort(sequencia)
    fim = time.time()
    print("Ordenação concluída.")

    print("Vetor ordenado:")
    print(sequencia)

    tempo_execucao = fim - inicio
    print(f"Tempo de execução: {tempo_execucao:.2f} segundos")

if __name__ == "__main__":
    main()