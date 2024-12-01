import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo subido
file_path = './data.csv'
data = pd.read_csv(file_path)

# Mostrar las primeras filas para entender el contenido del archivo
#print(data.head())

# Construir la tabla de frecuencias
frecuencia_absoluta = data['Productividad'].value_counts().sort_index()
frecuencia_relativa = frecuencia_absoluta / frecuencia_absoluta.sum()

tabla_frecuencias = pd.DataFrame({
    'Frecuencia Absoluta': frecuencia_absoluta,
    'Frecuencia Relativa': frecuencia_relativa
})

# Generar el diagrama de pastel
plt.figure(figsize=(8, 8))
frecuencia_absoluta.plot.pie(
    autopct='%1.1f%%',
    labels=['Muy Baja', 'Baja', 'Alta', 'Muy Alta'],
    colors=['lightcoral', 'gold', 'skyblue', 'limegreen'],
    startangle=90
)
plt.title('Diagrama de Pastel de Productividad')
plt.ylabel('')  # Quitar etiqueta del eje y para claridad
plt.show()

# Calcular el valor más representativo (moda)
valor_representativo = frecuencia_absoluta.idxmax()

print('Tabla de frecuencias: \n')
print(tabla_frecuencias) 
print('\n Valores representativos: \n')
print(valor_representativo)
