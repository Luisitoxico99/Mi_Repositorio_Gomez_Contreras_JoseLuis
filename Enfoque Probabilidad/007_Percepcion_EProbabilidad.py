import cv2

# Cargar una imagen
imagen = cv2.imread('ejemplo.jpg')

# Mostrar la imagen original
cv2.imshow('Imagen Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow('Imagen en Escala de Grises', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detectar bordes en la imagen utilizando el operador de Canny
bordes = cv2.Canny(imagen_gris, 100, 200)

# Mostrar los bordes detectados
cv2.imshow('Bordes Detectados', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
