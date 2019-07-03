from Board import Board
from Player import Player
from settings import *
import numpy as np


class Env():
    def __init__(self, player:Player, board:Board ):
        self.player = player
        self.board = board

    def step(self, action: int):
        self.player.move(action)
        r = self.player.update(self.board)

        position = self.player.body[0]

        up = 0
        if (position[1] == 0):
            up = 1

        right = 0
        if (position[0] == SIZE - 1):
            right = 1

        down = 0
        if (position[1] == SIZE - 1):
            down = 1

        left = 0
        if (position[0] == 0):
            left = 1

        state = np.array([up, right, down, left])
        state = np.roll(state, -1 * self.player.action + 1)

        done = self.player.alive == False
        return state, r, done
