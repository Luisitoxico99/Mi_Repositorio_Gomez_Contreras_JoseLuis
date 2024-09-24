# Diccionario para almacenar respuestas precargadas y nuevas
base_de_datos = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias. ¿Y tú?",
    "¿De qué te gustaría hablar?": "Podemos hablar de lo que quieras, ¡dime más!"
}

def chatbot(pregunta):
    if pregunta in base_de_datos:
        return base_de_datos[pregunta]
    else:
        nueva_respuesta = input(f"No tengo una respuesta para '{pregunta}'. ¿Cómo debería responder a esta pregunta? ")
        base_de_datos[pregunta] = nueva_respuesta
        return "Gracias, he aprendido algo nuevo."

def main():
    print("¡Hola! Soy tu chatbot. Escribe algo para iniciar la conversación.")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == "salir":
            print("Chatbot: ¡Adiós!")
            break
        respuesta = chatbot(pregunta)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()
