import cv2
import numpy as np

# Capturar video desde la cámara web
cap = cv2.VideoCapture(0)

# Leer el primer frame del video
ret, frame_anterior = cap.read()

# Convertir el frame anterior a escala de grises
gray_anterior = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)

# Definir el detector de movimiento (diferencia absoluta)
def detector_movimiento(frame_anterior, frame_actual):
    gray_actual = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)
    diferencia = cv2.absdiff(gray_anterior, gray_actual)
    _, umbral = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contornos:
        if cv2.contourArea(contorno) > 100:
            (x, y, w, h) = cv2.boundingRect(contorno)
            cv2.rectangle(frame_actual, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Ciclo principal
while True:
    # Leer el frame actual del video
    ret, frame_actual = cap.read()
    
    # Realizar el seguimiento de movimiento
    detector_movimiento(frame_anterior, frame_actual)
    
    # Mostrar el frame actual con el seguimiento de movimiento
    cv2.imshow('Seguimiento de Movimiento', frame_actual)
    
    # Actualizar el frame anterior con el frame actual
    frame_anterior = frame_actual.copy()
    
    # Salir del ciclo si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
