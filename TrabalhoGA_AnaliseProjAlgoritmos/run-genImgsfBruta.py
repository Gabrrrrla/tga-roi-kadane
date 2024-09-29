import pandas as pd
from fBruta import processar_arquivos as fBrutaGen
from utils import plot_export

dfs_fBruta = []

for i in range(0, 10):
    pasta_arquivos = 'TrabalhoGA_AnaliseProjAlgoritmos\in'
    df_fBruta = fBrutaGen(pasta_arquivos)
    plot_export(df_fBruta, f'fb{i+1}x', 'Força Bruta')
    dfs_fBruta.append(df_fBruta)

average_df_fBruta = pd.concat(dfs_fBruta).groupby(['Arquivo', 'Soma máxima'], as_index=False)['Tempo de execução (s)'].mean()

plot_export(average_df_fBruta, 'fbMedias', 'Força Bruta')