import pygame
pygame.init()
from gameObject import GameObject

# Configure the screen by defining height and width
# returns a screen object
screen = pygame.display.set_mode([500, 500])
ara = GameObject(120, 300, 'ara.png')

# game loop
running = True
while running: 
    # Look for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        
    # clear the screen
    screen.fill((255, 255, 255))
    ara.render(screen)
    # update the display
    pygame.display.flip()



    