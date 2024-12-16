from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, RoundedRectangle
from .chatbot import Chatbot
 # Importa Chatbot desde el archivo en la misma carpeta

# Clase para la pantalla inicial
class PreMenuConsulta(BoxLayout):
    def __init__(self, iniciar_consulta_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.iniciar_consulta_callback = iniciar_consulta_callback

        with self.canvas.before:
            Color(0.6, 1, 0.6, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(Label(text="Consultar", font_size=36, bold=True, size_hint=(1, 0.1)))

        nube = BoxLayout(size_hint=(1, 0.2), padding=10, spacing=10)
        with nube.canvas.before:
            Color(1, 1, 1, 1)
            RoundedRectangle(size=nube.size, pos=nube.pos, radius=[10])
        nube.bind(size=self._update_rect, pos=self._update_rect)
        nube.add_widget(Label(
            text="Hola, Soy el Dr. Agavin. Estoy aquí para ayudarte con tus cultivos tequileros.\n"
                 "Responderé tus preguntas y te proporcionaré recomendaciones útiles.",
            font_size=14,
        ))
        self.add_widget(nube)

        self.add_widget(Image(
            source="C:/Users/Administrador/Documents/CETI/7mo/Sistemas expertos/AgaveMedicalInsure/gui/OriginalAgavin.png",
            size_hint=(1, 0.4),
        ))

        iniciar_btn = Button(
            text="Iniciar Consulta",
            font_size=18,
            background_color=(0.5, 0.8, 0.5, 1),
            size_hint=(1, 0.1)
        )
        iniciar_btn.bind(on_press=lambda instance: self.iniciar_consulta_callback())
        self.add_widget(iniciar_btn)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# Clase del cuestionario
class Cuestionario(BoxLayout):
    def __init__(self, preguntas, finalizar_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.preguntas = preguntas
        self.pregunta_actual = 0
        self.respuestas = []
        self.finalizar_callback = finalizar_callback

        with self.canvas.before:
            Color(0.6, 1, 0.6, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(Label(
            text="Cuestionario del Dr. Agavin",
            font_size=24, bold=True, size_hint=(1, 0.1)
        ))

        self.imagen_agavin = Image(
            source="C:/Users/Administrador/Documents/CETI/7mo/Sistemas expertos/AgaveMedicalInsure/gui/OriginalAgavin.png",
            size_hint=(1, 0.3),
        )
        self.add_widget(self.imagen_agavin)

        self.pregunta_label = Label(
            text=self.preguntas[self.pregunta_actual]["pregunta"],
            font_size=18, size_hint=(1, 0.2)
        )
        self.add_widget(self.pregunta_label)

        self.respuesta_area = BoxLayout(size_hint=(1, 0.2))
        self.actualizar_respuesta()
        self.add_widget(self.respuesta_area)

        siguiente_btn = Button(
            text="Siguiente", size_hint=(1, 0.1),
            background_color=(0.5, 0.8, 0.5, 1)
        )
        siguiente_btn.bind(on_press=self.siguiente_pregunta)
        self.add_widget(siguiente_btn)

    def actualizar_respuesta(self):
        self.respuesta_area.clear_widgets()
        tipo = self.preguntas[self.pregunta_actual]["tipo"]
        if tipo == "cerrada":
            for opcion in self.preguntas[self.pregunta_actual]["opciones"]:
                btn = Button(
                    text=opcion, size_hint=(0.3, 1),
                    background_color=(0.7, 0.7, 1, 1),
                )
                btn.bind(on_press=lambda instance, opcion=opcion: self.responder(opcion))
                self.respuesta_area.add_widget(btn)
        elif tipo == "abierta":
            self.text_input = TextInput(
                hint_text="Escribe tu respuesta aquí...",
                size_hint=(1, 1), multiline=False
            )
            self.respuesta_area.add_widget(self.text_input)

    def responder(self, respuesta):
        self.respuestas.append(respuesta)

    def siguiente_pregunta(self, instance):
        if self.preguntas[self.pregunta_actual]["tipo"] == "abierta":
            respuesta = self.text_input.text.strip()
            if respuesta:
                self.respuestas.append(respuesta)
        self.pregunta_actual += 1
        if self.pregunta_actual < len(self.preguntas):
            self.pregunta_label.text = self.preguntas[self.pregunta_actual]["pregunta"]
            self.actualizar_respuesta()
        else:
            self.finalizar_callback(self.respuestas)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# Clase para resultados
class Resultado(BoxLayout):
    def __init__(self, diagnostico, menu_principal_callback, abrir_chatbot_callback, salir_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        with self.canvas.before:
            Color(0.6, 1, 0.6, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(Image(
            source="C:/Users/Administrador/Documents/CETI/7mo/Sistemas expertos/AgaveMedicalInsure/gui/OriginalAgavin.png",
            size_hint=(1, 0.3)
        ))

        self.add_widget(Label(
            text=f"Diagnóstico: {diagnostico}",
            font_size=18, size_hint=(1, 0.2)
        ))

        self.add_widget(Label(
            text="¿La solución fue satisfactoria?",
            font_size=16, size_hint=(1, 0.1)
        ))

        botones_layout = BoxLayout(size_hint=(1, 0.2))
        btn_si = Button(text="Sí", size_hint=(0.5, 1), background_color=(0, 1, 0, 1))
        btn_no = Button(text="No", size_hint=(0.5, 1), background_color=(1, 0, 0, 1))

        btn_si.bind(on_press=lambda instance: menu_principal_callback())
        btn_no.bind(on_press=lambda instance: abrir_chatbot_callback())

        botones_layout.add_widget(btn_si)
        botones_layout.add_widget(btn_no)
        self.add_widget(botones_layout)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# Aplicación principal
class ConsultarApp(App):
    def build(self):
        self.preguntas = [
            {"pregunta": "¿El color de las hojas es amarillo?", "tipo": "cerrada", "opciones": ["Sí", "No"]},
            {"pregunta": "¿Hay manchas marrones visibles?", "tipo": "cerrada", "opciones": ["Sí", "No"]},
            {"pregunta": "Describe otros síntomas:", "tipo": "abierta"},
        ]
        return PreMenuConsulta(self.iniciar_cuestionario)

    def iniciar_cuestionario(self):
        self.root.clear_widgets()
        self.root.add_widget(Cuestionario(self.preguntas, self.finalizar_cuestionario))

    def finalizar_cuestionario(self, respuestas):
        diagnostico = "Hongo identificado. Aplicar tratamiento antifúngico cada 2 semanas."
        self.root.clear_widgets()
        self.root.add_widget(Resultado(
            diagnostico,
            self.menu_principal,
            self.abrir_chatbot,
            self.salir_app
        ))

    def abrir_chatbot(self):
        self.root.clear_widgets()
        self.root.add_widget(Chatbot(self.menu_principal, self.salir_app))

    def menu_principal(self):
        self.stop()

    def salir_app(self):
        App.get_running_app().stop()


if __name__ == '__main__':
    ConsultarApp().run()
