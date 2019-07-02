import pygame

FPS = 60
SIZE = 30
TAIL = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((TAIL, TAIL), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.image.fill((255, 255, 0))


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()


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

    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()