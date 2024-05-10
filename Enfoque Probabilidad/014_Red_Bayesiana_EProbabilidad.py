from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura del grafo (DAG)
modelo = BayesianModel([('A', 'C'), ('B', 'C')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_C = TabularCPD(variable='C', variable_card=2,
                   values=[[0.8, 0.9, 0.3, 0.7],
                           [0.2, 0.1, 0.7, 0.3]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Añadir las CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C)

# Verificar la consistencia del modelo
print("¿El modelo es válido?", modelo.check_model())

# Realizar inferencia en el modelo
inference = VariableElimination(modelo)
probabilidad_C = inference.query(variables=['C'])
print(probabilidad_C)
