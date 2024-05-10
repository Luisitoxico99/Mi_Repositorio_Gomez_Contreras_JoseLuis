from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import numpy as np

class NodoArbolRegresion:
    def __init__(self, caracteristica=None, valor=None, modelos=None, verdadero=None, falso=None):
        self.caracteristica = caracteristica  # Característica utilizada para la división en este nodo
        self.valor = valor  # Valor de la característica para la división en este nodo
        self.modelos = modelos  # Modelos de regresión lineal en las hojas
        self.verdadero = verdadero  # Subárbol para valores verdaderos de la característica
        self.falso = falso  # Subárbol para valores falsos de la característica

def calcular_error(modelo, X, y):
    # Calcula el error cuadrático medio del modelo en el conjunto de datos
    y_pred = modelo.predict(X)
    error = np.mean((y_pred - y) ** 2)
    return error

def construir_arbol_regresion(X, y, caracteristicas, max_profundidad, min_muestras_split, min_muestras_hoja):
    if max_profundidad == 0 or len(np.unique(y)) == 1:  # Si se alcanza la profundidad máxima o todos los resultados son iguales
        modelo = LinearRegression()
        modelo.fit(X, y)
        return NodoArbolRegresion(modelos=[modelo])
    mejor_ganancia = 0
    mejor_caracteristica = None
    mejor_valor = None
    mejor_subconjunto_verdadero = None
    mejor_subconjunto_falso = None
    for i, caracteristica in enumerate(caracteristicas):
        valores_unicos = np.unique(X[:, i])
        for valor in valores_unicos:
            subconjunto_verdadero = X[X[:, i] <= valor]
            subconjunto_falso = X[X[:, i] > valor]
            if len(subconjunto_verdadero) < min_muestras_split or len(subconjunto_falso) < min_muestras_split:
                continue
            ganancia = calcular_ganancia_informacion(X, y, subconjunto_verdadero, subconjunto_falso)
            if ganancia > mejor_ganancia:
                mejor_ganancia = ganancia
                mejor_caracteristica = caracteristica
                mejor_valor = valor
                mejor_subconjunto_verdadero = subconjunto_verdadero
                mejor_subconjunto_falso = subconjunto_falso
    if mejor_ganancia == 0:  # Si no se puede hacer una división
        modelo = LinearRegression()
        modelo.fit(X, y)
        return NodoArbolRegresion(modelos=[modelo])
    nuevo_caracteristicas = [c for c in caracteristicas if c != mejor_caracteristica]
    nodo_verdadero = construir_arbol_regresion(mejor_subconjunto_verdadero, y[mejor_subconjunto_verdadero], nuevo_caracteristicas, max_profundidad - 1, min_muestras_split, min_muestras_hoja)
    nodo_falso = construir_arbol_regresion(mejor_subconjunto_falso, y[mejor_subconjunto_falso], nuevo_caracteristicas, max_profundidad - 1, min_muestras_split, min_muestras_hoja)
    return NodoArbolRegresion(caracteristica=mejor_caracteristica, valor=mejor_valor, verdadero=nodo_verdadero, falso=nodo_falso)

def calcular_ganancia_informacion(X, y, subconjunto_verdadero, subconjunto_falso):
    error_total = calcular_error(LinearRegression().fit(X, y), X, y)
    prop_verdadero = len(subconjunto_verdadero) / len(X)
    prop_falso = len(subconjunto_falso) / len(X)
    error_verdadero = calcular_error(LinearRegression().fit(subconjunto_verdadero, y[subconjunto_verdadero]), subconjunto_verdadero, y[subconjunto_verdadero])
    error_falso = calcular_error(LinearRegression().fit(subconjunto_falso, y[subconjunto_falso]), subconjunto_falso, y[subconjunto_falso])
    ganancia = error_total - (prop_verdadero * error_verdadero + prop_falso * error_falso)
    return ganancia

def predecir(arbol, muestra):
    if arbol.modelos is not None:  # Si es una hoja (nodo terminal)
        return arbol.modelos[0].predict([muestra])
    sub_arbol = arbol.verdadero if muestra[arbol.caracteristica] <= arbol.valor else arbol.falso
    return predecir(sub_arbol, muestra)

# Ejemplo de uso
datos = load_boston()
X = datos.data
y = datos.target
caracteristicas = datos.feature_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
arbol_regresion = construir_arbol_regresion(X_train, y_train, caracteristicas, max_profundidad=5, min_muestras_split=2, min_muestras_hoja=1)

# Ejemplo de predicción
muestra = X_test[0]
prediccion = predecir(arbol_regresion, muestra)
print("Predicción:", prediccion)
