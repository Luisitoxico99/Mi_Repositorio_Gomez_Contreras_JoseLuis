from sklearn import datasets
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

# Cargar un conjunto de datos de ejemplo (por ejemplo, el conjunto de datos Iris)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 1. Escalar los datos utilizando el filtro StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Normalizar los datos utilizando el filtro MinMaxScaler
min_max_scaler = MinMaxScaler()
X_normalized = min_max_scaler.fit_transform(X)

# 3. Filtrar características de baja varianza utilizando VarianceThreshold
selector = VarianceThreshold(threshold=0.2)
X_filtered = selector.fit_transform(X)

# 4. Reducir la dimensionalidad utilizando Análisis de Componentes Principales (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Imprimir los resultados de cada filtro
print("Datos originales:")
print(X[:5, :])
print("\nDatos escalados:")
print(X_scaled[:5, :])
print("\nDatos normalizados:")
print(X_normalized[:5, :])
print("\nDatos después de filtrar características de baja varianza:")
print(X_filtered[:5, :])
print("\nDatos después de aplicar PCA:")
print(X_pca[:5, :])
