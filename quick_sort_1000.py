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

# Algoritmo Quick Sort
def quick_sort(sequencia, low, high):
    if low < high:
        p = partition(sequencia, low, high)
        quick_sort(sequencia, low, p - 1)
        quick_sort(sequencia, p + 1, high)

def partition(sequencia, low, high):
    pivot = sequencia[high]
    i = low - 1
    for j in range(low, high):
        if sequencia[j] <= pivot:
            i += 1
            sequencia[i], sequencia[j] = sequencia[j], sequencia[i]
    sequencia[i + 1], sequencia[high] = sequencia[high], sequencia[i + 1]
    return i + 1

# Função para gerar um vetor aleatório sem repetição
def gerar_sequencia_aleatoria_sem_repeticao(tamanho):
    return Sequencia(random.sample(range(1, tamanho + 1), tamanho))

# Teste do algoritmo
def main():
    tamanho = 1000
    print(f"\nGerando vetor de {tamanho} elementos desordenados e sem repetição...")
    sequencia = gerar_sequencia_aleatoria_sem_repeticao(tamanho)
    print("Vetor desordenado:")
    print(sequencia)

    print("Iniciando a ordenação com Quick Sort...")
    inicio = time.time()
    quick_sort(sequencia, 0, len(sequencia) - 1)
    fim = time.time()
    print("Ordenação concluída.")

    print("Vetor ordenado:")
    print(sequencia)

    tempo_execucao = fim - inicio
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    main()