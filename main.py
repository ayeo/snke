import pygame
import numpy as np

FPS = 30
SIZE = 30
TAIL = 5

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((TAIL, TAIL), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.image.fill((255, 255, 0))
        self.moving_x = 0
        self.moving_y = 1

    def update(self, *args):
        if self.moving_y == 1:
            self.position = tuple(np.array(self.position) + (0, 1 * TAIL))
        if self.moving_y == -1:
            self.position = tuple(np.array(self.position) + (0, -1 * TAIL))
        if self.moving_x == 1:
            self.position = tuple(np.array(self.position) + (1 * TAIL, 0))
        if self.moving_x == -1:
            self.position = tuple(np.array(self.position) + (-1 * TAIL, 0))

        self.rect.center = self.position

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





player = Player((50, 50))
sprites = pygame.sprite.Group()
sprites.add(player)




running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.move()

    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    print(events)

    for event in pygame.event.get():
        print(event)
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()