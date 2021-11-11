import pygame
from pygame.sprite import Sprite

class GameObject(Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        # self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
    
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))
