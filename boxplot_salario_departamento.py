import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Dados de exemplo
df = pd.DataFrame({
    'departamento': ['RH', 'TI', 'TI', 'Financeiro', 'RH', 'Financeiro', 'TI', 'RH', 'Financeiro'],
    'salario': [3000, 5000, 4800, 4200, 3100, 4300, 5100, 2900, 4400]
})

plt.figure(figsize=(10, 6))
sns.boxplot(x='departamento', y='salario', data=df, palette='pastel')
plt.title('Salário por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário')
plt.xticks(rotation=45)
plt.grid(True)

# 👉 Salvar antes de exibir
plt.savefig('boxplot_salario_departamento.png', dpi=300, bbox_inches='tight')
plt.show()
