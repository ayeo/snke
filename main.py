from Cube import *
from Player import *

player = Player((10, 10), 30)

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
    if (player.alive):
        color = (255, 255, 0)
    else:
        color = (255, 0, 0)
    for position in player.body:
        cube = Cube(position, color)
        sprites.add(cube)

    sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()