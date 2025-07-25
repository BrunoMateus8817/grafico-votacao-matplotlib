import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Exemplo de dados
df = pd.DataFrame({
    'genero': ['Masculino', 'Feminino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Feminino', 'Masculino']
})

plt.figure(figsize=(6, 4))
sns.countplot(x='genero', data=df, palette='Set2')
plt.title('Distribuição por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.grid(True)

# 👉 Salvar o gráfico antes de mostrar
plt.savefig('grafico_distribuicao_genero.png', dpi=300, bbox_inches='tight')
plt.show()
