class LogicaPorDefecto:
    def __init__(self, afirmaciones_por_defecto):
        self.afirmaciones_por_defecto = afirmaciones_por_defecto

    def verificar_afirmacion(self, afirmacion):
        # Verificar si una afirmación es verdadera por defecto
        if afirmacion in self.afirmaciones_por_defecto:
            return True
        else:
            return False

    def revisar_afirmaciones(self, nueva_evidencia):
        # Revisar las afirmaciones a la luz de la nueva evidencia
        # Aquí podrías implementar lógica específica para revisar o retractar afirmaciones en función de la nueva evidencia
        pass

# Ejemplo de uso
afirmaciones_iniciales = ["p", "q"]
logica_por_defecto = LogicaPorDefecto(afirmaciones_iniciales)

# Verificar una afirmación
afirmacion = "p"
es_verdadera = logica_por_defecto.verificar_afirmacion(afirmacion)
print(f"¿La afirmación '{afirmacion}' es verdadera por defecto? {es_verdadera}")

# Revisar las afirmaciones con nueva evidencia
nueva_evidencia = ["not q"]
logica_por_defecto.revisar_afirmaciones(nueva_evidencia)
