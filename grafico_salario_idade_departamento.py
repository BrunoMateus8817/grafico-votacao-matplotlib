import plotly.express as px
import pandas as pd

# Exemplo de DataFrame
df = pd.DataFrame({
    'idade': [25, 32, 40, 28, 45, 36, 29, 41, 33, 39],
    'salario': [2500, 3200, 4000, 2800, 4700, 3900, 3100, 4300, 3400, 3600],
    'departamento': ['TI', 'RH', 'Financeiro', 'TI', 'RH', 'TI', 'Financeiro', 'RH', 'Financeiro', 'TI'],
    'desempenho': [7.5, 8.0, 9.0, 7.0, 9.5, 8.5, 7.8, 9.2, 8.1, 8.4],
    'genero': ['Masculino', 'Feminino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Feminino', 'Masculino', 'Feminino']
})

fig = px.scatter(
    df,
    x='idade',
    y='salario',
    color='departamento',
    size='desempenho',
    hover_data=['genero'],
    title='Salário vs Idade por Departamento'
)

# ✅ Salvar como imagem PNG (requer kaleido instalado)
fig.write_image('salario_vs_idade_departamento.png', width=800, height=600, scale=2)


fig.show()
