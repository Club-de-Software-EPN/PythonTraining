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

class Fantasma(Personaje):
    def __init__(self, posicionInicial: Posicion, screen) -> None:
        self.rutaImg = 'Proyectos/pygame/assets/img/fantasma.png'
        self.screen = screen
        self.fantasmaImg = pygame.image.load(self.rutaImg)
        super().__init__(posicionInicial)

    def dibujar(self):
        self.screen.blit(self.fantasmaImg, self.posicion.obtenerCoordenadas())