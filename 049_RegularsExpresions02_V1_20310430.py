
import re
texto = "son siete septimos las septimas partes mas de lo que tienes"

resultado = re.findall("[a-p]",texto)
print(resultado)