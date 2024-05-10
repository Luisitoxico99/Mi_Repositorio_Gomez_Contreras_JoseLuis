class KBLSistemaRecomendacion:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def recomendar_peliculas(self, usuario):
        recomendaciones = []
        for regla in self.base_conocimiento:
            if regla.cumple_condiciones(usuario):
                recomendaciones.append(regla.pelicula)
        return recomendaciones

class ReglaRecomendacion:
    def __init__(self, condiciones, pelicula):
        self.condiciones = condiciones
        self.pelicula = pelicula

    def cumple_condiciones(self, usuario):
        for condicion in self.condiciones:
            if not condicion(usuario):
                return False
        return True

# Definimos algunas funciones de condición
def gusta_accion(usuario):
    return usuario["genero_favorito"] == "acción"

def edad_adecuada(usuario):
    return usuario["edad"] >= 18

# Creamos la base de conocimiento
base_conocimiento = [
    ReglaRecomendacion([gusta_accion, edad_adecuada], "Terminator"),
    ReglaRecomendacion([gusta_accion], "Die Hard"),
    ReglaRecomendacion([edad_adecuada], "Pulp Fiction"),
]

# Creamos un usuario de ejemplo
usuario_ejemplo = {"genero_favorito": "acción", "edad": 25}

# Creamos el sistema de recomendación y obtenemos las recomendaciones
sistema_recomendacion = KBLSistemaRecomendacion(base_conocimiento)
recomendaciones = sistema_recomendacion.recomendar_peliculas(usuario_ejemplo)

print("Recomendaciones para el usuario:")
for pelicula in recomendaciones:
    print("-", pelicula)
