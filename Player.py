import pygame
import numpy as np
from settings import *

class Player():
    body = []
    alive = True

    def __init__(self, position, length):
        self.moving_x = 0
        self.moving_y = 1
        for x in range(length):
            self.body.append(position)


    def add_body(self):
        self.body.append(self.body[-1])


    def update(self, board):
        if (self.alive == False):
            return

        position = self.body[0]
        if self.moving_y == 1:
            position = tuple(np.array(position) + (0, 1))
        if self.moving_y == -1:
            position = tuple(np.array(position) + (0, -1))
        if self.moving_x == 1:
            position = tuple(np.array(position) + (1, 0))
        if self.moving_x == -1:
            position = tuple(np.array(position) + (-1, 0))

        if (position == board.snack):
            self.add_body()
            board.place_snack(self.body)


        if (self.check_collision(position)):
            self.body.pop()
            self.body.insert(0, position)
        else:
            self.alive = False


    def check_collision(self, position):
        if (position) in self.body:
            return False
        if (position[0] < 0 or position[0] >= SIZE):
            return False
        if (position[1] < 0 or position[1] >= SIZE):
            return False
        return True


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving_x = -1
            self.moving_y = 0
        elif keys[pygame.K_RIGHT]:
            self.moving_x = 1
            self.moving_y = 0
        elif keys[pygame.K_UP]:
            self.moving_x = 0
            self.moving_y = -1
        elif keys[pygame.K_DOWN]:
            self.moving_x = 0
            self.moving_y = 1
