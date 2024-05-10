import numpy as np

# Probabilidades de lluvia, sol y nubes
probabilidad_lluvia = 0.3
probabilidad_sol = 0.5
probabilidad_nubes = 0.2

# Utilidades asociadas a cada resultado (en este caso, llevar o no un paraguas)
utilidad_paraguas = -1  # Si llevas un paraguas y no llueve
utilidad_no_paraguas = -5  # Si no llevas un paraguas y llueve

# Calcular utilidad esperada para llevar un paraguas
utilidad_esperada_paraguas = (probabilidad_lluvia * utilidad_paraguas) + (1 - probabilidad_lluvia) * utilidad_no_paraguas

# Decisión: si la utilidad esperada de llevar un paraguas es mayor que la de no llevarlo, entonces lleva el paraguas
if utilidad_esperada_paraguas > utilidad_no_paraguas:
    print("Llevar un paraguas")
else:
    print("No llevar un paraguas")
