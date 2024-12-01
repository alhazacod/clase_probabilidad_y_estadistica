import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

# Cargar los datos del nuevo archivo subido
data = pd.read_csv('data.csv')

# Mostrar las primeras filas para entender la estructura del archivo
#print(data.head())

# Extraer los datos de la columna relevante
piezas_aceptables = data['Piezas aceptables']

# Calcular medidas de centro y dispersión
media = piezas_aceptables.mean()
mediana = piezas_aceptables.median()
moda = piezas_aceptables.mode().iloc[0]
varianza = piezas_aceptables.var()
desviacion_estandar = piezas_aceptables.std()
rango = piezas_aceptables.max() - piezas_aceptables.min()

# Calcular los percentiles para descartar el 15% inferior y el 12% superior
percentil_15 = np.percentile(piezas_aceptables, 15)
percentil_88 = np.percentile(piezas_aceptables, 100 - 12)

# Generar el histograma y el polígono de frecuencias
plt.figure(figsize=(14, 6))

# Histograma
plt.subplot(1, 2, 1)
plt.hist(piezas_aceptables, bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Piezas Aceptables')
plt.xlabel('Número de piezas aceptables')
plt.ylabel('Frecuencia')

# Polígono de frecuencias
plt.subplot(1, 2, 2)
frecuencia, bins = np.histogram(piezas_aceptables, bins=10)
bin_centers = (bins[:-1] + bins[1:]) / 2
plt.plot(bin_centers, frecuencia, marker='o', linestyle='-', color='blue')
plt.title('Polígono de Frecuencias')
plt.xlabel('Número de piezas aceptables')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Calcular medidas de forma
asimetria = skew(piezas_aceptables)
curtosis = kurtosis(piezas_aceptables)

print(f'Media: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Moda: {moda:.2f}')
print(f'Varianza: {varianza:.2f}')
print(f'Desviacion estandar: {desviacion_estandar:.2f}')
print(f'Rango: {rango:.2f}')
print(f'Percentil 15: {percentil_15:.2f}')
print(f'Percentil 88: {percentil_88:.2f}')
print(f'Asimetria: {asimetria:.2f}')
print(f'Curtosis: {curtosis:.2f}')

