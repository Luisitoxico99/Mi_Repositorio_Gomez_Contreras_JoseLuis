from keras.models import Sequential
from keras.layers import Dense

# Crear un modelo secuencial
modelo = Sequential()

# Añadir una capa oculta con función de activación ReLU
modelo.add(Dense(64, input_dim=100, activation='relu'))

# Añadir una capa oculta con función de activación Tangente Hiperbólica (Tanh)
modelo.add(Dense(64, activation='tanh'))

# Añadir una capa de salida con función de activación Sigmoide
modelo.add(Dense(10, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
