import matplotlib.pyplot as plt
import pandas as pd

# Exemplo de dados fictícios
df = pd.DataFrame({
    'data_admissao': [
        '2023-01-10', '2023-01-25', '2023-02-15', '2023-03-01',
        '2023-03-20', '2023-04-05', '2023-05-12', '2023-05-18',
        '2023-06-02', '2023-06-25'
    ]
})

df['data_admissao'] = pd.to_datetime(df['data_admissao'])
df['mes_ano'] = df['data_admissao'].dt.to_period('M').astype(str)
admissoes_por_mes = df['mes_ano'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
admissoes_por_mes.plot(kind='line', marker='o')
plt.title('Admissões ao Longo do Tempo')
plt.xlabel('Mês/Ano')
plt.ylabel('Número de Admissões')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# 👉 Salvar antes de exibir
plt.savefig('admissoes_ao_longo_do_tempo.png', dpi=300, bbox_inches='tight')
plt.show()
