import numpy as np

class NodoArbolDecision:
    def __init__(self, caracteristica=None, valor=None, resultados=None, verdadero=None, falso=None):
        self.caracteristica = caracteristica  # Característica utilizada para la división en este nodo
        self.valor = valor  # Valor de la característica para la división en este nodo
        self.resultados = resultados  # Contiene los resultados si es un nodo terminal (hoja)
        self.verdadero = verdadero  # Subárbol para valores verdaderos de la característica
        self.falso = falso  # Subárbol para valores falsos de la característica

def entropia(datos):
    # Calcula la entropía de un conjunto de datos
    clases, conteo = np.unique(datos[:, -1], return_counts=True)
    probabilidad = conteo / len(datos)
    entropia = -np.sum(probabilidad * np.log2(probabilidad))
    return entropia

def ganancia_informacion(datos, caracteristica_idx):
    # Calcula la ganancia de información de una característica en un conjunto de datos
    valores_caracteristica = np.unique(datos[:, caracteristica_idx])
    entropia_total = entropia(datos)
    ganancia = 0
    for valor in valores_caracteristica:
        datos_valor = datos[datos[:, caracteristica_idx] == valor]
        probabilidad_valor = len(datos_valor) / len(datos)
        entropia_valor = entropia(datos_valor)
        ganancia += probabilidad_valor * entropia_valor
    ganancia_informacion = entropia_total - ganancia
    return ganancia_informacion

def dividir_datos(datos, caracteristica_idx, valor):
    # Divide los datos en dos conjuntos basados en el valor de la característica
    datos_verdaderos = datos[datos[:, caracteristica_idx] == valor]
    datos_falsos = datos[datos[:, caracteristica_idx] != valor]
    return datos_verdaderos, datos_falsos

def construir_arbol(datos, caracteristicas):
    if len(np.unique(datos[:, -1])) <= 1:  # Si todos los resultados son del mismo tipo
        return NodoArbolDecision(resultados=np.unique(datos[:, -1])[0])
    if len(caracteristicas) == 0:  # Si no quedan características para dividir
        return NodoArbolDecision(resultados=np.argmax(np.bincount(datos[:, -1])))
    mejor_ganancia = 0
    mejor_caracteristica = None
    for i, caracteristica in enumerate(caracteristicas):
        ganancia = ganancia_informacion(datos, i)
        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor_caracteristica = caracteristica
    nodos_verdadero, nodos_falso = dividir_datos(datos, mejor_caracteristica, 1)
    nuevo_caracteristicas = [c for c in caracteristicas if c != mejor_caracteristica]
    verdadero = construir_arbol(nodos_verdadero, nuevo_caracteristicas)
    falso = construir_arbol(nodos_falso, nuevo_caracteristicas)
    return NodoArbolDecision(caracteristica=mejor_caracteristica, verdadero=verdadero, falso=falso)

def predecir(arbol, muestra):
    if arbol.resultados is not None:  # Si es un nodo terminal (hoja)
        return arbol.resultados
    valor = muestra[arbol.caracteristica]
    sub_arbol = arbol.verdadero if valor == arbol.valor else arbol.falso
    return predecir(sub_arbol, muestra)

# Ejemplo de uso
datos = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
])
caracteristicas = ['Caracteristica1', 'Caracteristica2']
arbol = construir_arbol(datos, caracteristicas)

# Ejemplo de predicción
muestra = np.array([1, 1])
prediccion = predecir(arbol, muestra)
print("Predicción:", prediccion)
