import sys
import os
import time
import pandas as pd
from utils import ler_matriz

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

    return pd.DataFrame(resultados)
