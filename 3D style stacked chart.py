import matplotlib.pyplot as plt
import numpy as np

# Dados dos anos e da popularidade de cada linguagem
years = ['2022', '2023', '2024', '2025', '2026']
python_data = np.array([70, 78, 84, 91, 96])
java_data = np.array([60, 64, 68, 70, 73])
js_data = np.array([75, 80, 83, 87, 90])

# Configuração da figura
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5

# Configuração do empilhamento manual das barras
bottom1 = python_data
bottom2 = python_data + java_data

# Criação das barras empilhadas com cores e bordas estilizadas
bars1 = ax.bar(years, python_data, bar_width, label='Python', color='#ffb3b3', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(years, java_data, bar_width, bottom=bottom1, label='Java', color='#b3b3ff', edgecolor='black', linewidth=0.5)
bars3 = ax.bar(years, js_data, bar_width, bottom=bottom2, label='JS', color='#b3e6b3', edgecolor='black', linewidth=0.5)

# Adicionando os valores correspondentes dentro de cada seção das barras
ax.bar_label(bars1, label_type='center', fontsize=10, fontweight='bold', color='black')
ax.bar_label(bars2, label_type='center', fontsize=10, fontweight='bold', color='black')
ax.bar_label(bars3, label_type='center', fontsize=10, fontweight='bold', color='black')

# Personalização dos eixos, título e grade
ax.set_title("Programming Trends", fontsize=16)
ax.set_ylabel("Popularity", fontsize=12)
ax.set_xlabel("Year", fontsize=12)
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adicionando legenda e ajustando o layout
ax.legend(title='Language', title_fontsize=12, loc='upper left')
plt.tight_layout()

# Exibição do gráfico
plt.show()