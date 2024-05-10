class Tarea:
    def __init__(self, nombre, condiciones, sub_tareas=[]):
        self.nombre = nombre
        self.condiciones = condiciones
        self.sub_tareas = sub_tareas

class RedJerarquicaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def planificar(self, tarea_actual):
        if self.satisfacer_condiciones(tarea_actual):
            for sub_tarea in tarea_actual.sub_tareas:
                self.planificar(sub_tarea)
            print("Ejecutando tarea:", tarea_actual.nombre)
        else:
            print("No se pueden satisfacer las condiciones para la tarea:", tarea_actual.nombre)

    def satisfacer_condiciones(self, tarea):
        # Implementar lógica para verificar si se pueden satisfacer las condiciones de la tarea
        return True

# Ejemplo de uso
limpiar_casa = Tarea("Limpiar Casa", ["sin_polvo", "sin_suciedad"], [
    Tarea("Limpiar Suelo", ["suelo_sucio"], [
        Tarea("Pasar Aspiradora", ["suelo_con_polvillo"]),
        Tarea("Fregar Suelo", ["suelo_con_suciedad"])
    ]),
    Tarea("Limpiar Ventanas", ["ventanas_sucias"], [
        Tarea("Lavar Cristales", ["cristales_opacos"])
    ])
])

red_tareas = RedJerarquicaTareas()
red_tareas.agregar_tarea(limpiar_casa)

# Planificar y ejecutar la tarea de limpiar la casa
red_tareas.planificar(limpiar_casa)
