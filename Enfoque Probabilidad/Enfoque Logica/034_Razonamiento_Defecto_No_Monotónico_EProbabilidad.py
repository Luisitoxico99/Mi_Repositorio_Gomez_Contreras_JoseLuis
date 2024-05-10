import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear variables lingüísticas
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de pertenencia
calidad.automf(3)
servicio.automf(3)
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Crear reglas
regla1 = ctrl.Rule(quality['poor'] | service['poor'], propina['baja'])
regla2 = ctrl.Rule(service['average'], propina['media'])
regla3 = ctrl.Rule(service['good'] | quality['good'], propina['alta'])

# Crear sistema de control difuso
sistema_propinas = ctrl.ControlSystem([regla1, regla2, regla3])
propinas = ctrl.ControlSystemSimulation(sistema_propinas)

# Pasar entradas al sistema y calcular salida
propinas.input['calidad'] = 6.5
propinas.input['servicio'] = 9.8
propinas.compute()

# Imprimir resultado
print("Propina sugerida:", propinas.output['propina'])
