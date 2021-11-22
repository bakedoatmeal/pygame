import pygame
from gameObject import GameObject
from treat import Treat
from cheese import Cheese
from player import Player
from bomb import Bomb
from chase import Chase
from random import randint, random

pygame.init()
pygame.font.init()

bg = pygame.image.load("./images/dogespace.jpeg")

# Configure the screen by defining height and width
# returns a screen object
screen = pygame.display.set_mode([600, 600])
font = pygame.font.SysFont('timesnewroman', 30)
score = 0
scoreDisplay = f'Score: {score}'
text = font.render(scoreDisplay, True, (255, 255, 255))
treat = Treat()
cheese = Cheese()
ara = Player()
choc = Bomb()
#moose = Chase()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
treat_sprites = pygame.sprite.Group()

#all_sprites.add(moose)
all_sprites.add(ara)
all_sprites.add(cheese)
all_sprites.add(treat)
all_sprites.add(choc)
treat_sprites.add(cheese)
treat_sprites.add(treat)

game_state = 'ready'
running = True

#game loop 
while running: 
    if game_state == 'ready':
        # display the game in a ready state
		# listen for events an event here should 
		# change game_state to 'playing'
		# set score to 0
		# reset or initialize the game objects
        screen.fill((255, 255, 255))
        screen.blit(bg, (0,0))
        instructions = font.render("Catch the cheese and treats, avoid the chocolate!", True, (255, 255, 255))
        screen.blit(instructions, (5, 150))
        start_text = font.render("Click to Play!", True, (255, 255, 255))
        screen.blit(start_text, (100, 250))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                game_state = 'playing'

    elif game_state == 'playing':
        # Look for events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    ara.left()
                    #moose.left()
                elif event.key == pygame.K_RIGHT:
                    ara.right()
                    #moose.right()
                elif event.key == pygame.K_UP:
                    ara.up()
                    #moose.up()
                elif event.key == pygame.K_DOWN:
                    ara.down()
                    #moose.down()
                
        # clear the screen
        screen.fill((255, 255, 255))
        screen.blit(bg, (0,0))
        screen.blit(text, (0,0))
        for entity in all_sprites:
            entity.move()
            entity.render(screen)

        # check for collisions
        treat_collide = pygame.sprite.spritecollideany(ara, treat_sprites)
        if treat_collide: 
            treat_collide.reset()
            treat.dy += 0.25
            cheese.dx += 0.25
            choc.dx += 0.25
            score += 1
            scoreDisplay = f'Score: {score}'
            text = font.render(scoreDisplay, True, (255, 255, 255))
            #print(scoreDisplay)

        if pygame.sprite.collide_rect(ara, choc):
            # for entity in all_sprites: 
            #     entity.reset()
            game_state = 'game_over'

    # if pygame.sprite.collide_circle(ara, moose):
    #     running = False

    elif game_state == 'game_over':
        screen.fill((255, 255, 255))
        screen.blit(bg, (0,0))
        game_over_text = font.render(f"Game Over! Your score was {score}", True, (255, 255, 255))
        screen.blit(game_over_text, (15,150))
        play_again_text = font.render(f"Click to quit, press a key to play again", True, (255, 255, 255))
        screen.blit(play_again_text, (15, 250))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
            if event.type == pygame.KEYDOWN:
                score = 0
                game_state = 'playing'
                for entity in all_sprites:
                    entity.reset()
                treat.resetSpeed()
                choc.resetSpeed()
                cheese.resetSpeed()


    # update the display
    pygame.display.flip()
    clock.tick(60)



    