import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

# Generar datos de ejemplo con 3 clústeres
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Visualizar los datos de ejemplo
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Datos de ejemplo')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Aplicar k-Means para el agrupamiento
kmeans = KMeans(n_clusters=3, random_state=42)
etiquetas_kmeans = kmeans.fit_predict(X)

# Visualizar los clústeres encontrados por k-Means
plt.scatter(X[:, 0], X[:, 1], c=etiquetas_kmeans, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=200, label='Centroides')
plt.title('Clustering con k-Means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

# Aplicar k-NN para encontrar los vecinos más cercanos
knn = NearestNeighbors(n_neighbors=3)
knn.fit(X)

# Encontrar los vecinos más cercanos para un punto de consulta
punto_consulta = np.array([[0, 0]])
distancias, indices = knn.kneighbors(punto_consulta)

# Visualizar los vecinos más cercanos
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.scatter(punto_consulta[:, 0], punto_consulta[:, 1], c='red', marker='x', s=200, label='Punto de consulta')
plt.scatter(X[indices, 0], X[indices, 1], c='green', marker='o', s=100, alpha=0.5, label='Vecinos más cercanos')
plt.title('Vecinos más cercanos con k-NN')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
