from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
import numpy as np

# Definir la estructura del grafo (DAG)
modelo = BayesianModel([('A', 'B'), ('A', 'C')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.3], [0.2, 0.8]], evidence=['A'], evidence_card=[2])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.5, 0.5], [0.1, 0.9]], evidence=['A'], evidence_card=[2])

# Añadir las CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C)

# Generar muestras de las variables ocultas utilizando muestreo aleatorio
num_muestras = 10000
muestras_ponderadas = []
for _ in range(num_muestras):
    muestra = modelo.get_sample()
    peso = cpd_A.get_values()[muestra['A']]
    muestras_ponderadas.append((muestra, peso))

# Calcular la probabilidad del evento B=1 dado A=1 mediante ponderación de verosimilitud
probabilidad_B_dado_A = sum(peso for (muestra, peso) in muestras_ponderadas if muestra['B'] == 1) / sum(peso for (_, peso) in muestras_ponderadas if muestra['A'] == 1)

print("La probabilidad de B=1 dado A=1 mediante ponderación de verosimilitud es:", probabilidad_B_dado_A)
