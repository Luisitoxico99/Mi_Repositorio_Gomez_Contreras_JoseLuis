class SistemaTransporteAutonomo:
    def __init__(self, ruta_planificada):
        self.ruta_planificada = ruta_planificada
        self.estado_actual = None

    def ejecutar_ruta(self):
        for accion in self.ruta_planificada:
            self.ejecutar_accion(accion)
            if self.detectar_desviacion():
                print("Desviación detectada. Iniciando replanificación.")
                self.replanificar_ruta()
                break

    def ejecutar_accion(self, accion):
        # Implementar lógica para ejecutar la acción
        pass

    def detectar_desviacion(self):
        # Implementar lógica para detectar desviaciones
        pass

    def replanificar_ruta(self):
        # Implementar lógica para generar una nueva ruta
        pass

# Ejemplo de uso
ruta_planificada = ['Moverse a', 'Moverse b', 'Moverse c']
sistema = SistemaTransporteAutonomo(ruta_planificada)
sistema.ejecutar_ruta()
