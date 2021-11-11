from random import randint
import random
from gameObject import GameObject

class Cheese(GameObject):
    def __init__(self):
        self.positions = [93, 218, 343]
        y = random.choice(self.positions)
        super(Cheese, self).__init__(0, 0, 'cheese.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check the y position
        if self.x > 500:
            self.reset()

    def reset(self):
        self.y = random.choice(self.positions)
        self.x = -64
