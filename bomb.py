from random import randint, choice
import random 
from gameObject import GameObject

class Bomb(GameObject):
    def __init__(self):
        self.positions = [93, 218, 343]
        y = random.choice(self.positions)
        super(Bomb, self).__init__(0, 0, 'chocolate.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.direction = 1
        self.reset()

    def move(self):
        if self.direction == 0:
            self.x += self.dx
        else: 
            self.x -= self.dx
        self.y += self.dy
        # check the y position
        if self.direction == 0 and self.x > 500 or self.direction == 1 and self.x < -70:
            self.reset()

    def reset(self):
        self.direction = choice([0,1])
        self.y = choice(self.positions)
        if self.direction == 0:
            self.x = -64
        else: 
            self.x = 564
        
