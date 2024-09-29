from kadane import processar_arquivos as kadaneGen
from utils import plot_show

pasta_arquivos = 'TrabalhoGA_AnaliseProjAlgoritmos\in'
df_kadane = kadaneGen(pasta_arquivos)
plot_show(df_kadane, 'Kadane')