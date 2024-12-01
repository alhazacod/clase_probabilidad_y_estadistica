import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos del archivo subido para inspeccionar su contenido
file_path = './data.csv'
data = pd.read_csv(file_path)

#print(data.head())

# a) Calcular estadísticos descriptivos
media_x = data['x'].mean()
desviacion_x = data['x'].std()
coef_var_x = (desviacion_x / media_x) * 100

media_y = data['y'].mean()
desviacion_y = data['y'].std()
coef_var_y = (desviacion_y / media_y) * 100

print(f"\nMedia: ({media_x}, {media_y}) \nDesviación Estándar: ({desviacion_x}, {desviacion_y}) \nCoeficiente de Variación: ({coef_var_x}, {coef_var_y})")

# b) Gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(data['x'], data['y'], color='blue', alpha=0.7, label='Datos')
plt.title('Gráfico de Dispersión: Temperatura vs Coeficiente de Eficacia')
plt.xlabel('Temperatura (°F)')
plt.ylabel('Coeficiente de Eficacia (mg/ft²)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# c) Coeficiente de correlación
correlacion = np.corrcoef(data['x'], data['y'])[0, 1]
