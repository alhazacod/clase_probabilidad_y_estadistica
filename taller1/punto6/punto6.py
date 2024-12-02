import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('./data.csv')  

# Calcular estadísticas para cada zona
def calculate_statistics(data, column_name):
    mean = data[column_name].mean()
    median = data[column_name].median()
    std_dev = data[column_name].std()
    coeff_var = (std_dev / mean) * 100
    return mean, median, std_dev, coeff_var

stats_pino = calculate_statistics(data, 'Pino suave')
stats_piedra = calculate_statistics(data, 'Piedra dura')

# Mostrar estadísticas
print("Estadísticas para Pino Suave:")
print(f"Media: {stats_pino[0]}, Mediana: {stats_pino[1]}, Desviación Estándar: {stats_pino[2]}, Coeficiente de Variación: {stats_pino[3]}")

print("\nEstadísticas para Piedra Dura:")
print(f"Media: {stats_piedra[0]}, Mediana: {stats_piedra[1]}, Desviación Estándar: {stats_piedra[2]}, Coeficiente de Variación: {stats_piedra[3]}")

# Generar boxplots
plt.figure(figsize=(10, 5))
plt.boxplot([data['Pino suave'], data['Piedra dura']], labels=['Pino Suave', 'Piedra Dura'], patch_artist=True)
plt.title("Boxplots de Pino Suave y Piedra Dura")
plt.ylabel("Mediciones")
plt.show()

# Generar diagrama de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(data['Pino suave'], data['Piedra dura'], color='blue', alpha=0.7)
plt.title("Diagrama de Dispersión: Pino Suave vs Piedra Dura")
plt.xlabel("Pino Suave")
plt.ylabel("Piedra Dura")
plt.grid(True)
plt.show()

