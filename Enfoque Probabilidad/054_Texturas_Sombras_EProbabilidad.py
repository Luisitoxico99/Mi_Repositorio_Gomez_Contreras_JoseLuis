import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Función para cargar una textura desde un archivo de imagen
def cargar_textura():
    textura_surface = pygame.image.load('textura.jpg')  # Cargar la textura desde un archivo de imagen
    textura_data = pygame.image.tostring(textura_surface, 'RGBA', 1)  # Convertir la textura en formato RGBA
    textura = glGenTextures(1)  # Generar un ID de textura
    glBindTexture(GL_TEXTURE_2D, textura)  # Vincular la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)  # Configurar el filtro de textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textura_surface.get_width(), textura_surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, textura_data)  # Establecer los datos de textura
    return textura

# Función para dibujar un cubo texturizado
def draw_textured_cube(textura):
    glBegin(GL_QUADS)
    # Cara frontal
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)
    # Continuar para las demás caras
    glEnd()

# Función para inicializar OpenGL
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
    glEnable(GL_COLOR_MATERIAL)

# Función principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    textura = cargar_textura()

    init()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 3, 1, 1)  # Rotar el cubo

        draw_textured_cube(textura)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
