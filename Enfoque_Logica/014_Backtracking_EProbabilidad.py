class NReinas:
    def __init__(self, N):
        self.N = N
        self.solucion = [-1] * N

    def es_seguro(self, fila, col):
        # Verifica si es seguro colocar una reina en la posición (fila, col)
        for i in range(fila):
            if self.solucion[i] == col or \
               self.solucion[i] - i == col - fila or \
               self.solucion[i] + i == col + fila:
                return False
        return True

    def resolver_n_reinas(self, fila):
        # Caso base: si todas las reinas están colocadas
        if fila == self.N:
            return True

        # Probar todas las columnas en esta fila
        for col in range(self.N):
            if self.es_seguro(fila, col):
                # Colocar una reina en esta posición
                self.solucion[fila] = col

                # Resolver para las filas restantes
                if self.resolver_n_reinas(fila + 1):
                    return True

                # Si no se encontró solución, retroceder y probar otra columna
                self.solucion[fila] = -1

        # Si no se puede colocar una reina en ninguna columna en esta fila
        return False

    def imprimir_solucion(self):
        for fila in range(self.N):
            fila_solucion = ""
            for col in range(self.N):
                if self.solucion[fila] == col:
                    fila_solucion += "Q "
                else:
                    fila_solucion += "_ "
            print(fila_solucion)
        print()

# Ejemplo de uso
N = 8
n_reinas = NReinas(N)
if n_reinas.resolver_n_reinas(0):
    print(f"Solución para {N} reinas:")
    n_reinas.imprimir_solucion()
else:
    print(f"No se encontró solución para {N} reinas.")
