from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
np.random.seed(0)
X = np.concatenate([np.random.normal(-2, 1, 500),
                    np.random.normal(2, 1, 500)]).reshape(-1, 1)

# Inicializar y ajustar el modelo K-Means con 2 clústeres
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Obtener las etiquetas de clúster para cada punto
etiquetas = kmeans.labels_

# Obtener los centroides de los clústeres
centroides = kmeans.cluster_centers_

# Visualizar los datos y los clústeres
plt.scatter(X, np.zeros_like(X), c=etiquetas, cmap='viridis', alpha=0.5)
plt.scatter(centroides, np.zeros_like(centroides), c='red', marker='x', s=100)
plt.title('Agrupamiento con K-Means')
plt.xlabel('Datos')
plt.ylabel('No se utiliza')
plt.show()
