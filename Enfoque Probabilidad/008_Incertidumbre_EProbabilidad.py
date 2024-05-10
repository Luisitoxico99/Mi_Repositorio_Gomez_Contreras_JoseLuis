import numpy as np

# Generar datos aleatorios que representan mediciones de una variable
datos = np.random.normal(loc=10, scale=2, size=1000)  # Media=10, Desviación estándar=2

# Calcular estadísticas descriptivas básicas
media = np.mean(datos)  # Calcular la media de los datos
varianza = np.var(datos)  # Calcular la varianza de los datos
desviacion_estandar = np.std(datos)  # Calcular la desviación estándar de los datos

# Imprimir las estadísticas descriptivas calculadas
print("Media:", media)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion_estandar)
