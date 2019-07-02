from Cube import *
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

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player.move()
    player.update(board)

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