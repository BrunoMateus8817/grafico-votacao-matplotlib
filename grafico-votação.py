import matplotlib.pyplot as plt
import numpy as np

# Dados da votação
dados = [100, 200, 50]
categorias = ['Sim', 'Não', 'Talvez']

# Destacar a barra de maior impacto visual ("Não")
highlight_index = 1  # índice do "Não"
cores = ['gray'] * len(categorias)
cores[highlight_index] = '#ff7f0e'  # cor de destaque

# Criar o gráfico
plt.figure(figsize=(8, 6))  # tamanho do gráfico
plt.bar(categorias, dados, color=cores)

# Título com mensagem interpretativa
plt.title("Maioria rejeita a proposta", fontsize=14, fontweight='bold')

# Rótulos dos eixos
plt.xlabel("Respostas", fontsize=12)
plt.ylabel("Quantidade de pessoas", fontsize=12)

# Linha de referência da meta
plt.axhline(150, color='gray', linestyle='--', linewidth=1)
plt.text(2.2, 150, 'Meta: 150 votos', color='gray')

# Inserir os valores acima das barras
for i, valor in enumerate(dados):
    plt.text(i, valor + 5, f'{valor}', ha='center', fontweight='bold')

# Remover grid para visual mais limpo
plt.grid(False)


# Salvar como imagem (opcional)
plt.savefig("grafico_votacao.png", dpi=300, bbox_inches='tight')

# Exibir
plt.show()
