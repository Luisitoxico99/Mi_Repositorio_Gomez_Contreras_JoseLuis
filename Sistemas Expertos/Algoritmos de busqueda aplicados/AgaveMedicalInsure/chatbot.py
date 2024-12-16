from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
import os
from difflib import get_close_matches


class Chatbot(BoxLayout):
    def __init__(self, menu_principal_callback, salir_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Ruta absoluta al archivo de datos
        self.data_file = os.path.join(os.path.dirname(__file__), "chatbot_respuestas_agave.txt")
        self.respuestas = self.cargar_respuestas()

        # Fondo verde
        with self.canvas.before:
            Color(0.6, 1, 0.6, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Imagen del Dr. Agavin
        self.add_widget(Image(
            source=os.path.join(os.path.dirname(__file__), "OriginalAgavin.png"),
            size_hint=(1, 0.3),
        ))

        # Título del chatbot
        self.add_widget(Label(
            text="Chatbot del Dr. Agavin", font_size=24, size_hint=(1, 0.1)
        ))

        # Área de conversación
        self.chat_area = BoxLayout(orientation='vertical', size_hint=(1, 0.4))
        self.add_widget(self.chat_area)

        # Entrada de usuario
        self.user_input = TextInput(
            hint_text="Escribe tu pregunta aquí...", size_hint=(1, 0.1), multiline=False
        )
        self.user_input.bind(on_text_validate=self.enviar_mensaje)
        self.add_widget(self.user_input)

        # Botón para enviar mensaje
        enviar_btn = Button(
            text="Enviar", size_hint=(1, 0.1), background_color=(0.5, 0.8, 0.5, 1)
        )
        enviar_btn.bind(on_press=self.enviar_mensaje)
        self.add_widget(enviar_btn)

        # Botones Menú Principal y Salir
        botones_layout = BoxLayout(size_hint=(1, 0.2))
        btn_menu = Button(text="Menú Principal", size_hint=(0.5, 1), background_color=(0.5, 0.8, 0.5, 1))
        btn_salir = Button(text="Salir", size_hint=(0.5, 1), background_color=(1, 0.5, 0.5, 1))
        btn_menu.bind(on_press=lambda instance: menu_principal_callback())
        btn_salir.bind(on_press=lambda instance: salir_callback())

        botones_layout.add_widget(btn_menu)
        botones_layout.add_widget(btn_salir)
        self.add_widget(botones_layout)

        # Mensaje de bienvenida
        self.mostrar_mensaje("¡Hola! Soy el Dr. Agavin. ¿En qué puedo ayudarte hoy?")

    def enviar_mensaje(self, instance):
        pregunta = self.user_input.text.strip().lower()
        if pregunta:
            self.limpiar_chat()
            self.mostrar_mensaje(f"Tú: {pregunta}")
            respuesta = self.generar_respuesta(pregunta)
            self.mostrar_mensaje(f"Dr. Agavin: {respuesta}")
            self.user_input.text = ""

    def generar_respuesta(self, pregunta):
        claves = list(self.respuestas.keys())
        coincidencias = get_close_matches(pregunta, claves, n=1, cutoff=0.6)

        if coincidencias:
            return self.respuestas[coincidencias[0]]

        return "Lo siento, no tengo una respuesta para eso."

    def cargar_respuestas(self):
        if not os.path.exists(self.data_file):
            print(f"Archivo de datos no encontrado: {self.data_file}")
            return {}
        with open(self.data_file, "r", encoding="utf-8") as f:
            return dict(line.strip().split(":", 1) for line in f if ":" in line)

    def mostrar_mensaje(self, texto):
        # Limpiar y mostrar nuevo mensaje
        self.chat_area.clear_widgets()
        self.chat_area.add_widget(self._crear_nube(texto))

    def limpiar_chat(self):
        # Elimina mensajes anteriores
        self.chat_area.clear_widgets()

    def _crear_nube(self, texto):
        nube = BoxLayout(size_hint=(1, None), height=50, padding=5)
        with nube.canvas.before:
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=nube.pos, size=nube.size, radius=[10])
        nube.add_widget(Label(text=texto, font_size=14, color=(0, 0, 0, 1)))
        return nube

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


if __name__ == '__main__':
    from kivy.app import App

    class ChatbotApp(App):
        def build(self):
            return Chatbot(lambda: print("Menú principal"), lambda: print("Salir"))

    ChatbotApp().run()
