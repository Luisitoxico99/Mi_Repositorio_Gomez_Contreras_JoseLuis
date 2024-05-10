class LogicaTemporal:
    def __init__(self, eventos):
        self.eventos = eventos

    def antes_de(self, evento1, evento2):
        # Verifica si evento1 ocurre antes de evento2 en la secuencia de eventos
        if evento1 in self.eventos and evento2 in self.eventos:
            return self.eventos.index(evento1) < self.eventos.index(evento2)
        else:
            return False

    def despues_de(self, evento1, evento2):
        # Verifica si evento1 ocurre después de evento2 en la secuencia de eventos
        if evento1 in self.eventos and evento2 in self.eventos:
            return self.eventos.index(evento1) > self.eventos.index(evento2)
        else:
            return False

# Ejemplo de uso
eventos = ["Despertar", "Desayunar", "Trabajar", "Almorzar", "Descansar"]
logica_temporal = LogicaTemporal(eventos)

# Consultas temporales
print("¿El evento 'Trabajar' ocurre antes que 'Almorzar'?", logica_temporal.antes_de("Trabajar", "Almorzar"))
print("¿El evento 'Desayunar' ocurre después que 'Descansar'?", logica_temporal.despues_de("Desayunar", "Descansar"))
