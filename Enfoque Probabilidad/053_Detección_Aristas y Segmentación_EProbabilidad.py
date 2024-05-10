import cv2
import numpy as np

# Cargar una imagen en escala de grises
imagen = cv2.imread('imagen.jpg', 0)

# Aplicar el detector de bordes Canny
bordes = cv2.Canny(imagen, 100, 200)

# Aplicar segmentación por umbralización
_, segmentacion = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes resultantes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Detección de Bordes (Canny)', bordes)
cv2.imshow('Segmentación (Umbralización)', segmentacion)
cv2.waitKey(0)
cv2.destroyAllWindows()
