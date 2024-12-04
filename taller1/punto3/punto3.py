import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

data = pd.read_csv('data.csv')
salarios = data['Salarios']
#print(salarios)

# Calcular medidas de centro
media = salarios.mean()
mediana = salarios.median()
moda = salarios.mode().iloc[0]

# Calcular medidas de dispersión
varianza = salarios.var()
desviacion_estandar = salarios.std()
rango = salarios.max() - salarios.min()

# Mostrar resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")
print(f"Rango: {rango}")

# Calcular medidas de forma
asimetria = skew(salarios)
curtosis = kurtosis(salarios)
print(f"Asimetría: {asimetria}")
print(f"Curtosis: {curtosis}")

# Crear un diagrama de forma (histograma)
plt.figure(figsize=(12, 6))
plt.hist(salarios, bins=10, color='skyblue', edgecolor='black')
plt.title('Diagrama de Forma (Histograma)')
plt.xlabel('Salarios (millones de pesos)')
plt.ylabel('Frecuencia')
plt.show()

# Crear un diagrama de tallos y hojas
def stem_and_leaf(data):
    """Crea un diagrama de tallos y hojas para los datos dados."""
    data = (data * 10).astype(int)  
    data = np.sort(data)
    stems = {}

    for num in data:
        stem, leaf = divmod(num, 10)
        stems.setdefault(stem, []).append(leaf)

    # Imprimir diagrama de tallos y hojas
    for stem, leaves in sorted(stems.items()):
        leaves_original = [leaf / 10 for leaf in leaves]
        print(f"{stem} | {' '.join(f'{leaf:.1f}' for leaf in leaves_original)}")

print("Diagrama de tallos y hojas:")
stem_and_leaf(salarios)
