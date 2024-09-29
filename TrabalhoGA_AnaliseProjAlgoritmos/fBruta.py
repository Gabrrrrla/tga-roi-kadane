import os
import time
import pandas as pd
from utils import ler_matriz

# Função para encontrar a soma máxima da submatriz
def maxSubmatrixSum(A):
    r = len(A)
    c = len(A[0])
    somaMax = float('-inf') # Menos infinito

    # Itera sobre todas as possíveis combinações de subretângulos
    for rStart in range(r):
        for cStart in range(c):
            for rEnd in range(rStart, r):
                for cEnd in range(cStart, c):
                    somaAtual = 0
                    for i in range(rStart, rEnd + 1):
                        for j in range(cStart, cEnd + 1):
                            somaAtual += A[i][j]
                    if somaAtual > somaMax:
                        somaMax = somaAtual

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
