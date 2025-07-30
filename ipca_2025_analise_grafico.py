import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados CSV exportados do IBGE
df = pd.read_csv('tabela3065 (1).csv.csv', sep=';', encoding='latin1', skiprows=3)


# Selecionar a linha com os dados reais (linha "BR")
dados_ipca = df.iloc[0]

# Nomes dos meses e extração dos valores
meses = ['janeiro 2025', 'fevereiro 2025', 'março 2025', 'abril 2025', 'maio 2025', 'junho 2025']
valores = [
    float(dados_ipca['Unnamed: 2'].replace(',', '.')),
    float(dados_ipca['Unnamed: 4'].replace(',', '.')),
    float(dados_ipca['Unnamed: 6'].replace(',', '.')),
    float(dados_ipca['Unnamed: 8'].replace(',', '.')),
    float(dados_ipca['Unnamed: 10'].replace(',', '.')),
    float(dados_ipca['Unnamed: 12'].replace(',', '.'))
]

# Gráfico da série histórica (linha)
plt.figure(figsize=(10, 5))
plt.plot(meses, valores, marker='o', linestyle='-', color='royalblue')
plt.title('Série Histórica IPCA-15 (jan a jun/2025)', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Número-Índice', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_ipca15_serie_historica.png', dpi=300, bbox_inches='tight')
plt.show()

# Cálculo da variação percentual mensal
variacao_percentual = np.diff(valores) / valores[:-1] * 100
meses_variacao = meses[1:]

# Gráfico da variação percentual mensal (barras)
plt.figure(figsize=(10, 5))
plt.bar(meses_variacao, variacao_percentual, color='darkorange')
plt.title('Variação Percentual Mensal do IPCA-15 (jan a jun/2025)', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Variação (%)', fontsize=12)
plt.grid(True, axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_ipca15_variacao_percentual.png', dpi=300, bbox_inches='tight')
plt.show()

# Cálculo da inflação acumulada no semestre
inflacao_acumulada = (valores[-1] / valores[0] - 1) * 100
print(f"Inflação acumulada no semestre: {inflacao_acumulada:.2f}%")
