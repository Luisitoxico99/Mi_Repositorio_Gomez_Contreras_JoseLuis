from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class MenuPrincipal(BoxLayout):
    def __init__(self, iniciar_consulta_callback, salir_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        with self.canvas.before:
            Color(0.6, 1, 0.6, 1)  # Fondo verde claro
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Título
        titulo = Label(
            text="Menú Principal",
            font_size=36,
            bold=True,
            size_hint=(1, 0.2),
            color=(0, 0, 0, 1),
            halign="center",
            valign="middle",
        )
        self.add_widget(titulo)

        # Imagen del Dr. Agavin
        imagen_agavin = Image(
            source="C:/Users/Administrador/Documents/CETI/7mo/Sistemas expertos/AgaveMedicalInsure/gui/OriginalAgavin.png",
            size_hint=(1, 0.4),
        )
        self.add_widget(imagen_agavin)

        # Botones de las opciones
        botones_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.4))

        opciones = [
            ("Escanear agave por medio de fotografías", self.opcion_1),
            ("Detectar enfermedad por consulta", iniciar_consulta_callback),
            ("Monitoreo de planta mediante el tiempo", self.opcion_3),
            ("Salud general de planta y conservación", self.opcion_4),
        ]
        for texto, callback in opciones:
            boton = Button(
                text=texto,
                font_size=18,
                size_hint=(1, 0.2),
                background_color=(0.5, 0.8, 0.5, 1),
            )
            boton.bind(on_release=callback)
            botones_layout.add_widget(boton)

        self.add_widget(botones_layout)

        # Botón de salir
        boton_salir = Button(
            text="Salir",
            font_size=18,
            size_hint=(1, 0.1),
            background_color=(1, 0, 0, 1),
        )
        boton_salir.bind(on_release=salir_callback)
        self.add_widget(boton_salir)

    def opcion_1(self, instance):
        print("Opción 1: Escanear agave por medio de fotografías seleccionada.")
        # Aquí se llamará al módulo de escaneo de imágenes

    def opcion_3(self, instance):
        print("Opción 3: Monitoreo de planta seleccionada.")
        # Aquí se implementará el monitoreo en el tiempo

    def opcion_4(self, instance):
        print("Opción 4: Salud general y conservación seleccionada.")
        # Aquí se desplegarán recomendaciones generales

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class AgaveApp(App):
    def build(self):
        return MenuPrincipal(
            iniciar_consulta_callback=self.iniciar_consulta,
            salir_callback=self.salir_app
        )

    def iniciar_consulta(self, instance):
        from gui.consultar import PreMenuConsulta
        self.root.clear_widgets()
        self.root.add_widget(PreMenuConsulta(iniciar_consulta_callback=self.mostrar_cuestionario))

    def mostrar_cuestionario(self):
        from gui.consultar import Cuestionario
        preguntas = [
            {"pregunta": "¿El color de las hojas es amarillo?", "tipo": "cerrada", "opciones": ["Sí", "No"]},
            {"pregunta": "¿Hay manchas marrones visibles?", "tipo": "cerrada", "opciones": ["Sí", "No"]},
            {"pregunta": "Describe otros síntomas:", "tipo": "abierta"},
        ]
        self.root.clear_widgets()
        self.root.add_widget(Cuestionario(preguntas=preguntas, finalizar_callback=self.mostrar_resultado))

    def mostrar_resultado(self, respuestas):
        from gui.consultar import Resultado
        diagnostico = "Hongo identificado. Aplicar tratamiento antifúngico cada 2 semanas."
        self.root.clear_widgets()
        self.root.add_widget(Resultado(
            diagnostico=diagnostico,
            menu_principal_callback=self.build,
            salir_callback=self.salir_app
        ))

    def salir_app(self, instance=None):
        print("Cerrando la aplicación")
        App.get_running_app().stop()

if __name__ == '__main__':
    AgaveApp().run()
