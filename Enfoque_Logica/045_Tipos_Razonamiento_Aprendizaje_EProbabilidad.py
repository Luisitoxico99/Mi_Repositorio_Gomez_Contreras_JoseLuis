from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Paso 1: Cargar el conjunto de datos (Iris dataset)
iris = load_iris()
X = iris.data  # características
y = iris.target  # etiquetas

# Paso 2: Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Crear el modelo de regresión logística
model = LogisticRegression()

# Paso 4: Entrenar el modelo utilizando el conjunto de entrenamiento
model.fit(X_train, y_train)

# Paso 5: Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Paso 6: Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
