from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador AdaBoost
# Se utiliza un clasificador de árbol de decisión como clasificador base (por defecto)
adaboost = AdaBoostClassifier(n_estimators=50, random_state=42)

# Entrenar el clasificador
adaboost.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = adaboost.predict(X_test)

# Calcular la precisión del clasificador
precision = accuracy_score(y_test, y_pred)
print("Precisión:", precision)
