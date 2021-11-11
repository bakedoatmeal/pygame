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
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check the y position
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = random.choice(self.positions)
        self.y = -64
