import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# Generar datos de ejemplo (círculos concéntricos)
X, y = make_circles(n_samples=100, noise=0.1, factor=0.5, random_state=42)

# Visualizar los datos de ejemplo
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', label='Clase 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Clase 1')
plt.title('Datos de ejemplo')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

# Inicializar y ajustar el modelo SVM con kernel RBF (Gaussiano)
svm = SVC(kernel='rbf', gamma='auto', random_state=42)
svm.fit(X, y)

# Función para visualizar los límites de decisión
def plot_decision_boundary(model, X, y):
    h = .02  # Paso de la malla
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.title('Límites de decisión del SVM con kernel RBF')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

# Visualizar los límites de decisión del SVM
plot_decision_boundary(svm, X, y)
