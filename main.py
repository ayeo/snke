import pygame
import numpy as np

FPS = 30
SIZE = 30
TAIL = 5

class Cube(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((TAIL, TAIL), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = tuple(np.array(self.position) * TAIL)
        self.image.fill((255, 255, 0))

class Player():
    body = []

    def __init__(self, position, length):
        self.moving_x = 0
        self.moving_y = 1
        for x in range(length):
            self.body.append(position)

    def update(self):
        position = self.body[0]
        if self.moving_y == 1:
            position = tuple(np.array(position) + (0, 1))
        if self.moving_y == -1:
            position = tuple(np.array(position) + (0, -1))
        if self.moving_x == 1:
            position = tuple(np.array(position) + (1, 0))
        if self.moving_x == -1:
            position = tuple(np.array(position) + (-1, 0))

        self.body.pop()
        self.body.insert(0, position)

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


player = Player((10, 10), 3)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player.move()
    player.update()

    sprites = pygame.sprite.Group()
    for part in player.body:
        cube = Cube(part)
        sprites.add(cube)

    sprites.draw(screen)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()