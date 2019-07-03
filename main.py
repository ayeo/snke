from Cube import *
from Env import Env
from Player import *
from Board import *

player = Player((10, 10), 2)
board = Board(SIZE)
board.place_snack(player.body)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()

env = Env(player, board)

done = False

while done == False:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        s, r, done = env.step(2)
    elif keys[pygame.K_RIGHT]:
        s, r, done = env.step(1)
    else:
        s, r, done = env.step(0)


    sprites = pygame.sprite.Group()
    if (player.alive):
        color = (255, 255, 0)
    else:
        color = (255, 0, 0)
    for position in player.body:
        cube = Cube(position, color)
        sprites.add(cube)

    sprites.add(Cube(board.snack, (0, 255, 0)))

    sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()