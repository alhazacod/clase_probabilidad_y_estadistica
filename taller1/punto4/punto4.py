import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency

# Cargar los datos
data = pd.read_csv('data.csv')

color_preferido = data.columns[0]
uso_color = data.columns[1]

# Crear tabla de contingencia
contingencia = pd.crosstab(data[color_preferido], data[uso_color])

# Visualización: Gráfico de barras apiladas
fig, ax = plt.subplots(figsize=(10, 6))
contingencia.plot(kind='bar', stacked=True, ax=ax, color=plt.cm.viridis(np.linspace(0, 1, contingencia.shape[1])))
ax.set_title('Relación entre Color Preferido y Uso del Color')
ax.set_xlabel('Color Preferido')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))

# Calcular proporciones para el mosaico
total = contingencia.sum().sum()
x_start = 0

for idx, (color, row) in enumerate(contingencia.iterrows()):
    y_start = 0
    for uso, value in row.items():
        width = row.sum() / total
        height = value / row.sum()
        ax.bar(x_start, height, width=width, align='edge', label=f'{uso}' if idx == 0 else "", color=plt.cm.viridis(np.linspace(0, 1, contingencia.shape[1]))[list(row.keys()).index(uso)])
        y_start += height
    x_start += width

ax.set_title('Mosaico: Relación entre Color Preferido y Uso del Color')
ax.set_xlabel('Color Preferido')
ax.set_ylabel('Proporción')
ax.legend(title='Uso del Color')
plt.tight_layout()
plt.show()

# Calcular el valor de V de Cramer
chi2, p, dof, expected = chi2_contingency(contingencia)
n = contingencia.sum().sum()
v_cramer = np.sqrt(chi2 / (n * (min(contingencia.shape) - 1)))

# Imprimir resultados
print(f"Chi-cuadrado: {chi2:.2f}")
print(f"p-valor: {p:.4f}")
print(f"V de Cramer: {v_cramer:.4f}")


