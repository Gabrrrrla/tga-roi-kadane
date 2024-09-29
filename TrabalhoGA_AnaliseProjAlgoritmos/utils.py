import os
import matplotlib.pyplot as plt
import dataframe_image as dfi

def plot_export(df, nomeArq, algoritmo):
    # Cria a pasta 'out' se não existir
    if not os.path.exists('out'):
        os.makedirs('out')
    
    tabela_path = os.path.join('out', f'{nomeArq}-tabela.png')
    grafico_path = os.path.join('out', f'{nomeArq}-grafico.png')

    dfi.export(df, tabela_path, table_conversion='matplotlib')

    plt.figure(figsize=(10, 6))
    plt.bar(df['Arquivo'], df['Tempo de execução (s)'], color='skyblue')
    plt.xlabel('Arquivo')
    plt.ylabel('Tempo de execução (s)')
    plt.title(f'Tempo de execução por arquivo - {algoritmo}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(grafico_path)

def plot_show(df, algoritmo):
    print("\nTabela de resultados:")
    print(df)

    plt.figure(figsize=(10, 6))
    plt.bar(df['Arquivo'], df['Tempo de execução (s)'], color='skyblue')
    plt.xlabel('Arquivo')
    plt.ylabel('Tempo de execução (s)')
    plt.title(f'Tempo de execução por arquivo - {algoritmo}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def ler_matriz(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        tamanho = int(linhas[0].strip())
        matriz = []
        for i in range(1, tamanho + 1):
            linha = list(map(int, linhas[i].strip().split()))
            matriz.append(linha)
    return matriz