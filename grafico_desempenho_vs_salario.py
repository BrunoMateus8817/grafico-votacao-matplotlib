import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'salario': [2500, 3000, 3500, 4000, 4500, 5000],
    'desempenho': [7.0, 7.5, 8.0, 8.5, 9.0, 9.5]
})

sns.scatterplot(x='desempenho', y='salario', data=df)
plt.title('Desempenho vs Salário')
plt.xlabel('Desempenho')
plt.ylabel('Salário')
plt.grid(True)
plt.savefig('desempenho_vs_salario.png', dpi=300, bbox_inches='tight')
plt.show()
