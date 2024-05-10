from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en datos de entrenamiento y de prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el clasificador Naïve Bayes
clf_nb = GaussianNB()

# Entrenar el clasificador Naïve Bayes con los datos de entrenamiento
clf_nb.fit(X_entrenamiento, y_entrenamiento)

# Realizar predicciones con los datos de prueba
predicciones = clf_nb.predict(X_prueba)

# Calcular la precisión del clasificador Naïve Bayes
precision = accuracy_score(y_prueba, predicciones)

print("Precisión del clasificador Naïve Bayes:", precision)
