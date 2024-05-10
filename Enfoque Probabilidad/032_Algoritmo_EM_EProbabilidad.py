from sklearn.mixture import GaussianMixture
import numpy as np

# Generar datos de ejemplo
np.random.seed(0)
X = np.concatenate([np.random.normal(-2, 1, 500),
                    np.random.normal(2, 1, 500)]).reshape(-1, 1)

# Inicializar y ajustar un modelo de mezcla gaussiana (GMM) con 2 componentes
gmm = GaussianMixture(n_components=2, random_state=0)
gmm.fit(X)

# Imprimir los parámetros estimados del modelo
print("Pesos de los componentes:", gmm.weights_)
print("Medias de los componentes:", gmm.means_)
print("Covarianzas de los componentes:", gmm.covariances_)
