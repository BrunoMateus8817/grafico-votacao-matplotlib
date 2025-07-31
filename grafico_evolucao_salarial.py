import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'salario': [2500, 2600, 2700, 2800, 2850, 2900]
})

plt.plot(df['mes'], df['salario'], marker='o')
plt.title('Evolução Salarial de Funcionário X')
plt.xlabel('Mês')
plt.ylabel('Salário')
plt.grid(True)
plt.savefig('evolucao_salarial_funcionario.png', dpi=300, bbox_inches='tight')
plt.show()
