import pygame
from Personajes.Personajes import Fantasma, Monstruo
from Personajes.Posicion import Posicion

dimensionesPantalla = (600,500)
colorFondo = (215, 255, 54)
posicionesIniciales = {
    'monstruo': Posicion((0,0)),
    'fantasma': Posicion((100,50))
}

# Inicialización de una instancia pygame
pygame.init()

# Configuraciones juego
pygame.display.set_caption('Monstruos')

# Creando una pantalla de juego
screen = pygame.display.set_mode(dimensionesPantalla)

# Bucle principal del juego
finalizado = False

# Inicialización personajes
fantasma = Fantasma(posicionesIniciales['fantasma'], screen)
monstruo = Monstruo(posicionesIniciales['monstruo'], screen)

while not finalizado:
    # Escenografía básica
    screen.fill(colorFondo)

    # Eventos (gestor de eventos de pygame)
    for event in pygame.event.get():
        # Evento cerrar una ventana
        if event.type == pygame.QUIT:
            finalizado = True
    # Render elementos
    # Elementos dinámicos
    fantasma.dibujar()
    monstruo.dibujar()
    # Actualizar la pantalla
    pygame.display.update()
