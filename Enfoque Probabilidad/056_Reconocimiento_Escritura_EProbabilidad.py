import pytesseract
from PIL import Image

# Cargar la imagen que contiene el texto manuscrito
imagen = Image.open('texto_manuscrito.png')

# Realizar el reconocimiento de escritura utilizando Tesseract
texto_reconocido = pytesseract.image_to_string(imagen, lang='eng')

# Imprimir el texto reconocido
print("Texto Reconocido:")
print(texto_reconocido)
