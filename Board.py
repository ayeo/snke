import random

class Board():
    def __init__(self, size):
        self.size = size

    def place_snack(self, body):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        if ((y, x) in body):
            return self.place_snack(body)
        else:
            self.snack = (y, x)