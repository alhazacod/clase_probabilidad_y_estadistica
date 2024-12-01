import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd

# Cargar el archivo para entender el contenido
file_path = './data.csv'
data = pd.read_csv(file_path)

#print(data.head())

# Renombrar columnas para facilidad de uso
data.rename(columns={'Unnamed: 0': 'Causa'}, inplace=True)

# Crear diagramas de pastel condicionales por fila
def plot_pie_charts(data):
    for index, row in data.iterrows():
        plt.figure(figsize=(6, 6))
        plt.pie(row[1:], labels=row.index[1:], autopct='%1.1f%%', startangle=90)
        plt.title(f"Distribución para {row['Causa']}")
        plt.show()

# Crear diagrama de barras segmentadas
def plot_segmented_bar_chart(data):
    column_totals = data.iloc[:, 1:].sum(axis=0)
    normalized_data = data.iloc[:, 1:].div(column_totals, axis=1)
    
    bar_width = 0.8
    indices = np.arange(len(data['Causa']))
    bottom_values = np.zeros(len(data['Causa']))
    
    plt.figure(figsize=(10, 6))
    for col in normalized_data.columns:
        plt.bar(indices, normalized_data[col], bar_width, bottom=bottom_values, label=col)
        bottom_values += normalized_data[col]
    
    plt.title("Diagrama de barras segmentadas")
    plt.ylabel("Proporción")
    plt.xticks(ticks=indices, labels=data['Causa'], rotation=0)
    plt.legend(title="Rangos")
    plt.tight_layout()
    plt.show()

# Calcular el valor de V de Cramer
def calculate_cramers_v(data):
    contingency_table = data.iloc[:, 1:].values
    chi2, p, dof, _ = chi2_contingency(contingency_table)
    n = contingency_table.sum()
    cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
    return cramers_v

# Generar gráficos
plot_pie_charts(data)
plot_segmented_bar_chart(data)

# Calcular y mostrar V de Cramer
v_cramer = calculate_cramers_v(data)
print("V de Cramer:", v_cramer)

