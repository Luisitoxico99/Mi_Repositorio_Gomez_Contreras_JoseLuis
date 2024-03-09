
import re

texto = "Un elefante se columpiaba sobre la tela de una - aranaaaaa"
resultado = re.sub(" ","---",texto,4)

print(resultado)