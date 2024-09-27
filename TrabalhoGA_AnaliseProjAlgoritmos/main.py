import sys
import os
import time
import pandas as pd
import matplotlib.pyplot as plt


def ler_matriz(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

        tamanho = int(linhas[0].strip())

        matriz = []

        for i in range(1, tamanho + 1):
            linha = list(map(int, linhas[i].strip().split()))
            matriz.append(linha)

    return matriz


# Função para encontrar a soma máxima contínua no vetor
def kadane(v):
    somaAtual = 0
    somaMax = -sys.maxsize - 1

    # Percorre o array v
    for i in range(len(v)):
        somaAtual += v[i]
        if somaAtual > somaMax:
            somaMax = somaAtual
        if somaAtual < 0:
            somaAtual = 0

    return somaMax


# Função para encontrar a soma máxima da submatriz
def maxSubmatrixSum(A):
    r = len(A)
    c = len(A[0])

    # Matriz auxiliar para armazenar a soma prefixada
    prefixo = [[0 for i in range(c)] for j in range(r)]

    # Calcula a soma prefixada para todas as linhas da matriz
    for i in range(r):
        for j in range(c):
            if j == 0:
                prefixo[i][j] = A[i][j]
            else:
                prefixo[i][j] = A[i][j] + prefixo[i][j - 1]

    somaMax = -sys.maxsize - 1

    # Itera sobre todas as possíveis combinações de colunas
    for i in range(c):
        for j in range(i, c):
            v = []

            # Percorre todas as linhas
            for k in range(r):
                if i == 0:
                    el = prefixo[k][j]
                else:
                    el = prefixo[k][j] - prefixo[k][i - 1]
                v.append(el)

            somaMax = max(somaMax, kadane(v))

    return somaMax


def processar_arquivos(pasta):

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]

    resultados = []

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        print(f"Processando arquivo: {arquivo}")

        inicio_tempo = time.time()

        matrix = ler_matriz(caminho_completo)

        max_sum = maxSubmatrixSum(matrix)

        tempo_execucao = time.time() - inicio_tempo

        resultados.append({
            'Arquivo': arquivo,
            'Soma máxima': max_sum,
            'Tempo de execução (s)': tempo_execucao
        })

    df_resultados = pd.DataFrame(resultados)

    print("\nTabela de resultados:")
    print(df_resultados)

    plt.figure(figsize=(10, 6))
    plt.bar(df_resultados['Arquivo'], df_resultados['Tempo de execução (s)'], color='skyblue')
    plt.xlabel('Arquivo')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Tempo de execução por arquivo')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

pasta_arquivos = 'in'
processar_arquivos(pasta_arquivos)
