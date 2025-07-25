import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Exemplo de DataFrame
df = pd.DataFrame({
    'idade': [25, 32, 40, 28, 45, 36, 29, 41, 33, 39],
    'salario': [2500, 3200, 4000, 2800, 4700, 3900, 3100, 4300, 3400, 3600],
    'desempenho': [7.5, 8.0, 9.0, 7.0, 9.5, 8.5, 7.8, 9.2, 8.1, 8.4]
})

plt.figure(figsize=(8, 5))
sns.heatmap(df[['idade', 'salario', 'desempenho']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação entre Variáveis')

# 👉 Salvar antes de mostrar
plt.savefig('correlacao_variaveis.png', dpi=300, bbox_inches='tight')
plt.show()
