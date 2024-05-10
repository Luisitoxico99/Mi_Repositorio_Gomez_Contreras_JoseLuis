# Implementación de un problema de planificación simple utilizando STRIPS en Python
class STRIPS:
    def __init__(self, estado_inicial, estado_objetivo, acciones):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.acciones = acciones

    def planificar(self):
        plan = []
        estado_actual = self.estado_inicial
        while estado_actual != self.estado_objetivo:
            accion_aplicable = None
            for accion in self.acciones:
                if accion.puede_aplicar(estado_actual):
                    accion_aplicable = accion
                    break
            if accion_aplicable is None:
                raise Exception("No se puede alcanzar el estado objetivo")
            plan.append(accion_aplicable)
            estado_actual = accion_aplicable.aplicar(estado_actual)
        return plan

class Accion:
    def __init__(self, precondiciones, efectos):
        self.precondiciones = precondiciones
        self.efectos = efectos

    def puede_aplicar(self, estado):
        return all(p in estado for p in self.precondiciones)

    def aplicar(self, estado):
        nuevo_estado = set(estado)
        for efecto in self.efectos:
            if efecto[0] == '-':
                nuevo_estado.discard(efecto[1:])
            else:
                nuevo_estado.add(efecto)
        return nuevo_estado

# Ejemplo de uso
estado_inicial = {'en_casa', 'despierto'}
estado_objetivo = {'en_trabajo'}
acciones = [
    Accion({'en_casa', 'despierto'}, {'en_trabajo'}),
    Accion({'en_trabajo'}, {'en_casa'})
]

problema = STRIPS(estado_inicial, estado_objetivo, acciones)
plan = problema.planificar()
print("Plan:", [str(accion) for accion in plan])
