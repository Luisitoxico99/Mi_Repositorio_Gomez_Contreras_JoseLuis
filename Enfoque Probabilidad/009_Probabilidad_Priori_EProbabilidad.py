# Definir una lista de eventos posibles
eventos_posibles = ['A', 'B', 'C']

# Definir una lista de observaciones
observaciones = ['A', 'B', 'A', 'A', 'C', 'B', 'A']

# Contar la frecuencia de cada evento en las observaciones
frecuencia_eventos = {}
for evento in eventos_posibles:
    frecuencia_eventos[evento] = observaciones.count(evento)

# Calcular la probabilidad a priori de cada evento
total_observaciones = len(observaciones)
probabilidad_a_priori = {}
for evento, frecuencia in frecuencia_eventos.items():
    probabilidad_a_priori[evento] = frecuencia / total_observaciones

# Imprimir la probabilidad a priori de cada evento
for evento, probabilidad in probabilidad_a_priori.items():
    print("Probabilidad a priori de {}: {:.2f}".format(evento, probabilidad))
