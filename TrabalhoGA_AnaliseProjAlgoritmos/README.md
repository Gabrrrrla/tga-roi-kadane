#  Identificando a Região de Interesse de uma Imagem
Ana Beatriz Stahl e Gabriela Bley Rodrigues - Análise e Projeto de Algoritmos - Profa. Andriele Busatto do Carmo

A solução proposta utiliza um algoritmo de força bruta e uma adaptação do algoritmo de Kadane para identificar a região de interesse (ROI) em imagens, focando em encontrar submatrizes que apresentam a maior soma de intensidades de pixel.

## Dependências
Para rodar este projeto é necessário instalar as seguintes bibliotecas Python:
- `pandas`
- `matplotlib`
- `dataframe_image`

Você pode instalar todas as dependências usando o seguinte comando:

```
pip install pandas matplotlib dataframe_image
```

## Como Rodar

### Executar o algoritmo de força bruta uma vez
Para rodar o algoritmo de força bruta, execute o arquivo `run-fBrutaOnce.py` através do seguinte comando no terminal:

```
python run-fBrutaOnce.py
```

### Executar o algoritmo de kadane uma vez
Para rodar o algoritmo de kadane, execute o arquivo `run-kadaneOnce.py` através do seguinte comando no terminal:

```
python run-kadaneOnce.py
```

### Executar o algoritmo de força bruta dez vezes e gerar imagens
Para rodar o algoritmo de força bruta dez vezes e exportar gráficos e tabelas para cada execução, bem como para as médias, execute o arquivo `run-genImgsfBruta.py`:

```
python run-genImgsfBruta.py
```

### Executar o algoritmo de kadane dez vezes e gerar imagens
Para rodar o algoritmo de kadane dez vezes e exportar gráficos e tabelas para cada execução, bem como para as médias, execute o arquivo `run-genImgsKadane.py`:

```
python run-genImgsKadane.py
```