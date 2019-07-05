from Cube import Cube
from Player import Player
from settings import *

import numpy as np
import pygame
import random

class Env():
    snack = (0, 0)
    pygame_inited = False


    def __init__(self, size: int):
        self.size = size


    def reset(self):
        self.player = Player((START_X, START_Y), INITIAL_LENGTH)
        self.place_snack(self.player.body)
        return self.state()


    def state(self):
        position = self.player.body[0]
        up = 0
        if (position[1] == 0 or list(position) + [-1, 0] in self.player.body):
            up = 1

        right = 0
        if (position[0] == SIZE - 1 or list(position) + [0, 1] in self.player.body):
            right = 1

        down = 0
        if (position[1] == SIZE - 1 or list(position) + [1, 0] in self.player.body):
            down = 1

        left = 0
        if (position[0] == 0 or list(position) + [0, -1] in self.player.body):
            left = 1

        state = np.array([up, right, down, left])
        state = np.roll(state, -1 * self.player.action + 1)
        state = np.delete(state, 2)  # remove down

        xx = self.snack
        up = 0
        if (position[0] == xx[0] and position[1] > xx[1]):
            up = 1

        right = 0
        if (position[1] == xx[1] and position[0] < xx[0]):
            right = 1

        down = 0
        if (position[0] == xx[0] and position[1] < xx[1]):
            down = 1

        left = 0
        if (position[1] == xx[1] and position[0] > xx[0]):
            left = 1

        food = np.array([up, right, down, left])
        food = np.roll(food, -1 * self.player.action + 1)
        food = np.delete(food, 2)  # remove down

        return np.array([state, food]).reshape(6)


    def step(self, action: int):
        self.player.move(action)
        r = self.player.update(self)
        done = self.player.alive == False
        return self.state(), r, done


    def render(self):
        if (self.pygame_inited == False):
            pygame.init()
            pygame.mixer.init()
            self.screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
            pygame.display.set_caption("Snke")
            self.clock = pygame.time.Clock()
            self.pygame_inited = True

        self.screen.fill((0, 0, 0))
        pygame.event.get()
        self.clock.tick(FPS)
        self._sprites().draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(50)



    def _sprites(self):
        sprites = pygame.sprite.Group()
        if (self.player.alive):
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)

        for position in self.player.body:
            cube = Cube(position, color)
            sprites.add(cube)

        sprites.add(Cube(self.snack, (0, 255, 0)))
        return sprites


    def place_snack(self, body):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        if ((y, x) in body):
            return self.place_snack(body)
        else:
            self.snack = (y, x)