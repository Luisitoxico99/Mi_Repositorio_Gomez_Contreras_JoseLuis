from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# Crear un modelo secuencial
modelo = Sequential()

# Añadir capas ocultas y de salida
modelo.add(Dense(64, input_dim=10, activation='relu'))
modelo.add(Dense(32, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo con el optimizador SGD y la función de pérdida de entropía cruzada binaria
modelo.compile(optimizer=SGD(lr=0.01), loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo con los datos de entrada X_train y las etiquetas y_train
modelo.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
