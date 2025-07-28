import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'departamento': ['TI', 'RH', 'Financeiro', 'TI', 'RH', 'Financeiro'],
    'salario': [3000, 2800, 3200, 5000, 3100, 4500]
})

media_por_departamento = df.groupby('departamento')['salario'].mean().sort_values()

media_por_departamento.plot(kind='barh', color='teal')
plt.title('Média Salarial por Departamento')
plt.xlabel('Salário Médio')
plt.ylabel('Departamento')
plt.grid(True)
plt.tight_layout()
plt.savefig('media_salarial_por_departamento.png', dpi=300, bbox_inches='tight')
plt.show()
