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

# Algoritmo Insertion Sort
def insertion_sort(sequencia):
    for i in range(1, len(sequencia)):
        chave = sequencia[i]
        j = i - 1
        while j >= 0 and chave < sequencia[j]:
            sequencia[j + 1] = sequencia[j]
            j -= 1
        sequencia[j + 1] = chave

# Função para gerar um vetor aleatório sem repetição
def gerar_sequencia_aleatoria_sem_repeticao(tamanho):
    return Sequencia(random.sample(range(1, tamanho + 1), tamanho))

# Teste do algoritmo
def main():
    tamanho = 100
    print(f"\nGerando vetor de {tamanho} elementos desordenados e sem repetição...")
    sequencia = gerar_sequencia_aleatoria_sem_repeticao(tamanho)
    print("Vetor desordenado:")
    print(sequencia)

    print("Iniciando a ordenação com Insertion Sort...")
    inicio = time.time()
    insertion_sort(sequencia)
    fim = time.time()
    print("Ordenação concluída.")

    print("Vetor ordenado:")
    print(sequencia)

    tempo_execucao = fim - inicio
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    main()