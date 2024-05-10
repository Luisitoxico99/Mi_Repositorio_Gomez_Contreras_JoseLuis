import cv2
import numpy as np

# Cargar el modelo MobileNet SSD pre-entrenado
net = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco.pbtxt')

# Lista de clases (categorías) disponibles en el modelo
classes = ["background", "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light", 
           "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", 
           "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", 
           "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", 
           "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", 
           "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", 
           "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", 
           "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

# Función para detectar objetos en una imagen
def detect_objects(image):
    blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    return detections

# Función para mostrar los objetos detectados en una imagen
def mostrar_objetos(image, detections, threshold=0.5):
    height, width, _ = image.shape
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > threshold:
            class_id = int(detections[0, 0, i, 1])
            class_name = classes[class_id]
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            label = "{}: {:.2f}%".format(class_name, confidence * 100)
            cv2.putText(image, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

# Cargar una imagen
image = cv2.imread('imagen.jpg')

# Detectar objetos en la imagen
detections = detect_objects(image)

# Mostrar los objetos detectados en la imagen
image_with_detections = mostrar_objetos(image.copy(), detections)

# Mostrar la imagen con los objetos detectados
cv2.imshow("Objetos Detectados", image_with_detections)
cv2.waitKey(0)
cv2.destroyAllWindows()
