from pyclips import Environment, Symbol

# Creamos un nuevo entorno de CLIPS
env = Environment()

# Definimos los conjuntos difusos y las reglas de inferencia difusa
codigo_clips = """
(deffuzzy altura
   (var alto (triangular 1 1.75 2))
   (var medio (triangular 1.5 2 2.5))
   (var bajo (triangular 2 2.25 3))
)

(deffuzzy peso
   (var ligero (triangular 50 60 70))
   (var medio (triangular 60 70 80))
   (var pesado (triangular 70 80 90))
)

(defrule regla1
   (altura alto)
   (peso ligero)
   =>
   (assert (delgadez alta))
)

(defrule regla2
   (altura medio)
   (peso medio)
   =>
   (assert (delgadez media))
)

(defrule regla3
   (altura bajo)
   (peso pesado)
   =>
   (assert (delgadez baja))
)
"""

# Cargamos el código CLIPS en el entorno
env.build(codigo_clips)

# Ejecutamos las reglas
env.run()

# Obtenemos los resultados de la inferencia
resultados = env.eval("(find-all-facts ((?f delgadez)) TRUE)")

# Imprimimos los resultados
print("Resultados de la inferencia:")
for resultado in resultados:
    print(resultado)
