import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Exemplo de dados com possíveis outliers
df = pd.DataFrame({
    'salario': [2500, 3000, 2800, 3500, 3200, 2900, 2700, 10000, 3300, 3100]
})

plt.figure(figsize=(6, 4))
sns.boxplot(y='salario', data=df, color='salmon')
plt.title('Outliers nos Salários')
plt.ylabel('Salário')
plt.grid(True)

# 👉 Salvar imagem
plt.savefig('boxplot_outliers_salario.png', dpi=300, bbox_inches='tight')
plt.show()
