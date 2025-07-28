import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'departamento': ['TI', 'RH', 'Financeiro', 'TI', 'RH', 'Financeiro', 'TI', 'RH']
})

contagem = df['departamento'].value_counts()

plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporção por Departamento')
plt.axis('equal')
plt.savefig('proporcao_departamento.png', dpi=300, bbox_inches='tight')
plt.show()
