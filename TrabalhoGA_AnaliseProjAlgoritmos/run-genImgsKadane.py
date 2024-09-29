import pandas as pd
from kadane import processar_arquivos as kadaneGen
from utils import plot_export

dfs_kadane = []

for i in range(0, 10):
    pasta_arquivos = 'TrabalhoGA_AnaliseProjAlgoritmos\in'
    df_kadane = kadaneGen(pasta_arquivos)
    plot_export(df_kadane, f'kadane{i+1}x', 'Kadane')
    dfs_kadane.append(df_kadane)

average_df_kadane = pd.concat(dfs_kadane).groupby(['Arquivo', 'Soma máxima'], as_index=False)['Tempo de execução (s)'].mean()

plot_export(average_df_kadane, 'kadaneMedias', 'Kadane')