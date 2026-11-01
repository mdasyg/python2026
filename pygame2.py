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

x=350
y=250   
velocity_x=10
velocity_y=15


while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("Left arrow key is pressed")
        x -= velocity_x
    if keys[pygame.K_RIGHT]:
        print("Right arrow key is pressed")
        x += velocity_x
    if keys[pygame.K_UP]:
        print("Up arrow key is pressed")
        y -= velocity_y
    if keys[pygame.K_DOWN]:
        print("Down arrow key is pressed")
        y += velocity_y

    if x < 0:
        x = 0
    if y < 0:
        y = 0   
    if x > size[0] - 20:
        x = size[0] - 20
    if y > size[1] - 55:
        y = size[1] - 55

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [x, y, 20, 55])
    #pygame.draw.ellipse(screen, GREEN, [55, 50, 20, 25])
    #pygame.draw.line(screen, BLUE, [0, 0], [100, 100], 5)
    #pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    pygame.display.flip()
    clock.tick(30)