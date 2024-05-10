class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class PlanificadorCondicional:
    def __init__(self, acciones):
        self.acciones = acciones

    def planificar(self, estado_actual, objetivo):
        plan = []
        while estado_actual != objetivo:
            accion_seleccionada = None
            for accion in self.acciones:
                if accion.precondiciones <= estado_actual and accion.efectos <= objetivo:
                    accion_seleccionada = accion
                    break
            if accion_seleccionada:
                plan.append(accion_seleccionada)
                estado_actual = estado_actual - accion_seleccionada.precondiciones + accion_seleccionada.efectos
            else:
                print("No se pudo encontrar una acción para avanzar hacia el objetivo.")
                break
        return plan

# Ejemplo de uso
acciones = [
    Accion("Moverse a", {"en_casa"}, {"en_trabajo"}),
    Accion("Moverse b", {"en_casa"}, {"en_trabajo"})
]
planificador = PlanificadorCondicional(acciones)
estado_actual = {"en_casa"}
objetivo = {"en_trabajo"}
plan = planificador.planificar(estado_actual, objetivo)
print("Plan:", [accion.nombre for accion in plan])
