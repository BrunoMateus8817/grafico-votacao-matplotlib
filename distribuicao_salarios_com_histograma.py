import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'salário': [2500, 3000, 4000, 3500, 3200, 2900, 2000, 4500, 3800, 4100, 3700]
})

plt.figure(figsize=(8, 5))
sns.histplot(df['salário'], kde=True, color='skyblue')
plt.title('Distribuição dos Salários')
plt.xlabel('Salário')
plt.ylabel('Frequência')
plt.grid(True)

# 👉 Salvar o gráfico ANTES de mostrar
plt.savefig('grafico_salarios.png', dpi=300, bbox_inches='tight')

# 👉 Mostrar o gráfico na tela
plt.show()
