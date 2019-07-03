import numpy as np
from settings import *

class Player():
    def __init__(self, position, length):
        self.moving_x = 0
        self.moving_y = 1
        self.action = 3
        self.body = []
        self.alive = True
        self.action = 0
        self.length = 0
        for x in range(length):
            self.body.append(position)


    def add_body(self):
        self.body.append(self.body[-1])


    def update(self, board) -> float:
        self.length += 1

        if (self.length == 1000):
            return -10

        if (self.alive == False):
            return 0

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
            self.length = 0
            return 10


        if (self.check_collision(position)):
            self.body.pop()
            self.body.insert(0, position)
            return .01
        else:
            self.alive = False
            return -100


    def check_collision(self, position):
        if (position) in self.body:
            return False
        if (position[0] < 0 or position[0] >= SIZE):
            return False
        if (position[1] < 0 or position[1] >= SIZE):
            return False
        return True


    def move(self, action):
        allowed = [0, 2, 4]
        action = allowed[action]

        if (action == 0):
            return

        x = [1, 2, 3, 4]
        action = np.roll(x, action - self.action - 2)[0]

        if action == 1: #up
            self.moving_x = 0
            self.moving_y = -1
            self.action = 1
        if action == 2: #right
            self.moving_x = 1
            self.moving_y = 0
            self.action = 2
        if action == 3: #down
            self.moving_x = 0
            self.moving_y = 1
            self.action = 3
        if action == 4: #left
            self.moving_x = -1
            self.moving_y = 0
            self.action = 4
