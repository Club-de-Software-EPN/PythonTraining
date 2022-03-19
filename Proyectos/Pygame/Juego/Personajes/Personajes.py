import pygame
from abc import ABC, abstractmethod

from Personajes.Posicion import Posicion

class Personaje(ABC):
    def __init__(self, posicionInicial: Posicion) -> None:
        super().__init__()
        self.posicion = posicionInicial

    @abstractmethod
    def dibujar(self):
        pass

class Monstruo(Personaje):
    def __init__(self, posicionInicial: Posicion, screen) -> None:
        self.rutaImg = 'Proyectos/pygame/assets/img/monstruo.png'
        self.screen = screen
        self.monstruoImg = pygame.image.load(self.rutaImg)
        self.monstruoImg = pygame.transform.scale(self.monstruoImg, (100,100))
        super().__init__(posicionInicial)

    def dibujar(self):
        self.screen.blit(self.monstruoImg, self.posicion.obtenerCoordenadas())

class Fantasma(Personaje):
    def __init__(self, posicionInicial: Posicion, screen) -> None:
        self.rutaImg = 'Proyectos/pygame/assets/img/fantasma.png'
        self.screen = screen
        self.fantasmaImg = pygame.image.load(self.rutaImg)
        self.fantasmaImg = pygame.transform.scale(self.fantasmaImg, (100,100))
        super().__init__(posicionInicial)

    def dibujar(self):
        self.screen.blit(self.fantasmaImg, self.posicion.obtenerCoordenadas())