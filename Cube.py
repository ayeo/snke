import pygame
import numpy as np

from settings import *

class Cube(pygame.sprite.Sprite):
    def __init__(self, position, color):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((TAIL, TAIL), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = tuple(np.array(self.position) * TAIL)
        self.image.fill(color)