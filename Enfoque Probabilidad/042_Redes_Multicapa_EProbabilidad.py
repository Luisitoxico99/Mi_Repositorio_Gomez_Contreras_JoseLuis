from keras.models import Sequential
from keras.layers import Dense

# Crear un modelo secuencial
modelo = Sequential()

# Añadir una capa oculta con 64 neuronas y función de activación ReLU
modelo.add(Dense(64, input_dim=10, activation='relu'))

# Añadir otra capa oculta con 32 neuronas y función de activación ReLU
modelo.add(Dense(32, activation='relu'))

# Añadir una capa de salida con 1 neurona y función de activación Sigmoide
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Resumen del modelo
modelo.summary()
