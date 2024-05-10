import tensorflow as tf

# Definir los datos de entrenamiento
x_train = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=tf.float32)
y_train = tf.constant([[0], [1], [1], [0]], dtype=tf.float32)

# Definir la arquitectura de la red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=1000, verbose=0)

# Evaluar el modelo
loss, accuracy = model.evaluate(x_train, y_train)
print("Pérdida:", loss)
print("Precisión:", accuracy)

# Hacer predicciones
predictions = model.predict(x_train)
print("Predicciones:")
for i in range(len(predictions)):
    print("Entrada:", x_train[i].numpy(), "Predicción:", predictions[i][0])
