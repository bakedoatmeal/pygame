import pygame
pygame.init()
from gameObject import GameObject
from treat import Treat
from cheese import Cheese
from player import Player

# Configure the screen by defining height and width
# returns a screen object
screen = pygame.display.set_mode([500, 500])
treat = Treat()
cheese = Cheese()
ara = Player()
clock = pygame.time.Clock()

# game loop
running = True
while running: 
    # Look for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                ara.left()
            elif event.key == pygame.K_RIGHT:
                ara.right()
            elif event.key == pygame.K_UP:
                ara.up()
            elif event.key == pygame.K_DOWN:
                ara.down()
            
    # clear the screen
    screen.fill((255, 255, 255))
    cheese.move()
    cheese.render(screen)
    treat.move()
    treat.render(screen)
    ara.move()
    ara.render(screen)
    # update the display
    pygame.display.flip()
    clock.tick(60)



    