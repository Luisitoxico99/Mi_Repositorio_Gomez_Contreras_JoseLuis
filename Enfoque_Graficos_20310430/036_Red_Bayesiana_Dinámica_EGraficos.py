from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la DBN
dbn = DBN()

# Agregar nodos para cada capa temporal
dbn.add_edges_from([
    (('X_t', 0), ('X_t+1', 0)),
    (('X_t', 0), ('Y_t', 0)),
    (('X_t+1', 0), ('Y_t+1', 0))
])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_X_t = TabularCPD(('X_t', 0), 2, [[0.7], [0.3]])
cpd_X_t1 = TabularCPD(('X_t+1', 0), 2, [[0.9, 0.3], [0.1, 0.7]], evidence=[('X_t', 0)], evidence_card=[2])
cpd_Y_t = TabularCPD(('Y_t', 0), 2, [[0.8, 0.4], [0.2, 0.6]], evidence=[('X_t', 0)], evidence_card=[2])
cpd_Y_t1 = TabularCPD(('Y_t+1', 0), 2, [[0.9, 0.2], [0.1, 0.8]], evidence=[('X_t+1', 0)], evidence_card=[2])

# Agregar CPDs a la DBN
dbn.add_cpds(cpd_X_t, cpd_X_t1, cpd_Y_t, cpd_Y_t1)

# Verificar la consistencia del modelo
print("Consistencia del modelo:", dbn.check_model())

# Imprimir la estructura de la DBN
print("Estructura de la DBN:")
print(dbn.edges())

# Imprimir los CPDs de la DBN
print("\nCPDs de la DBN:")
for cpd in dbn.get_cpds():
    print(cpd)
