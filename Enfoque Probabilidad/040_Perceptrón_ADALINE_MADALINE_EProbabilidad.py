class MADALINE:
    def __init__(self, n_entradas, n_salidas, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.zeros((n_entradas + 1, n_salidas))  # Inicializar los pesos (incluyendo el sesgo)

    def predict(self, entradas):
        suma_ponderada = np.dot(entradas, self.pesos[1:, :]) + self.pesos[0, :]  # Calcular la suma ponderada de las entradas
        return suma_ponderada

    def entrenar(self, X, y):
        for _ in range(self.epocas):
            for entrada, etiqueta in zip(X, y):
                salida = self.predict(entrada)
                error = etiqueta - salida
                self.pesos[1:, :] += self.tasa_aprendizaje * error * entrada[:, None]  # Actualizar los pesos
                self.pesos[0, :] += self.tasa_aprendizaje * error  # Actualizar el sesgo

                class ADALINE:
    def __init__(self, n_entradas, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.zeros(n_entradas + 1)  # Inicializar los pesos (incluyendo el sesgo)

    def predict(self, entradas):
        suma_ponderada = np.dot(entradas, self.pesos[1:]) + self.pesos[0]  # Calcular la suma ponderada de las entradas
        return suma_ponderada

    def entrenar(self, X, y):
        for _ in range(self.epocas):
            for entrada, etiqueta in zip(X, y):
                salida = self.predict(entrada)
                error = etiqueta - salida
                self.pesos[1:] += self.tasa_aprendizaje * error * entrada  # Actualizar los pesos
                self.pesos[0] += self.tasa_aprendizaje * error  # Actualizar el sesgo
