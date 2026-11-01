import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size=(700, 500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My Game2026")

done = False
clock = pygame.time.Clock()

while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [55, 50, 20, 25])
    pygame.draw.ellipse(screen, GREEN, [55, 50, 20, 25])
    pygame.draw.line(screen, BLUE, [0, 0], [100, 100], 5)
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    pygame.display.flip()
    clock.tick(30)