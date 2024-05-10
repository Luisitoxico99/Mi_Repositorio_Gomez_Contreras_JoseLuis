import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Función para dibujar un cubo
def draw_cube():
    glBegin(GL_QUADS)
    # Cara frontal
    glColor3fv((1, 0, 0))
    glVertex3fv((1, 1, -1))
    glVertex3fv((-1, 1, -1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((1, -1, -1))
    # Otras caras
    glColor3fv((0, 1, 0))
    glVertex3fv((1, -1, -1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((1, -1, 1))
    # Continuar para las demás caras
    glEnd()

# Función para inicializar OpenGL
def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800/600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)  # Mover la cámara hacia atrás

# Función para manejar los eventos del teclado
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.1, 0, 0)  # Mover hacia la izquierda
            elif event.key == pygame.K_RIGHT:
                glTranslatef(0.1, 0, 0)  # Mover hacia la derecha
            elif event.key == pygame.K_UP:
                glTranslatef(0, 0.1, 0)  # Mover hacia arriba
            elif event.key == pygame.K_DOWN:
                glTranslatef(0, -0.1, 0)  # Mover hacia abajo

# Función principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init()

    while True:
        handle_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 3, 1, 1)  # Rotar el cubo

        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
