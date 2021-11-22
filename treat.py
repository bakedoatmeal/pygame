from random import randint, random
from gameObject import GameObject
import random

class Treat(GameObject):
    def __init__(self):
        self.positions = [93, 218, 343]
        x = random.choice(self.positions)
        super(Treat, self).__init__(0, 0, 'treat.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.direction = 0
        self.reset()

    def move(self):
        self.x += self.dx
        if self.direction == 0:
            self.y += self.dy
        else: 
            self.y -= self.dy
        # check the y position
        if self.direction == 0 and self.y > 500 or self.direction == 1 and self.y < -50:
            self.reset()

    def reset(self):
        self.direction = random.choice([0,1])
        self.x = random.choice(self.positions)
        if self.direction == 0:
            self.y = -64
        else: 
            self.y = 564
        
    def resetSpeed(self):
        self.dy = (randint(0, 200) / 100) + 1
