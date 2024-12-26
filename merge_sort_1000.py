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

# Algoritmo Merge Sort
def merge_sort(sequencia):
    if len(sequencia) > 1:
        mid = len(sequencia) // 2
        L = Sequencia(sequencia.elementos[:mid])
        R = Sequencia(sequencia.elementos[mid:])

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sequencia[k] = L[i]
                i += 1
            else:
                sequencia[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            sequencia[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            sequencia[k] = R[j]
            j += 1
            k += 1

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

    print("Iniciando a ordenação com Merge Sort...")
    inicio = time.time()
    merge_sort(sequencia)
    fim = time.time()
    print("Ordenação concluída.")

    print("Vetor ordenado:")
    print(sequencia)

    tempo_execucao = fim - inicio
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    main()
