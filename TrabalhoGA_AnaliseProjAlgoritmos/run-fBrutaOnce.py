from fBruta import processar_arquivos as fBrutaGen
from utils import plot_show

pasta_arquivos = 'TrabalhoGA_AnaliseProjAlgoritmos\in'
df_fBruta = fBrutaGen(pasta_arquivos)
plot_show(df_fBruta, 'Força Bruta')