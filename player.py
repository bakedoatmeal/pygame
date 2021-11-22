from gameObject import GameObject
from random import randint, choice

lanes = [13, 138, 263, 388, 513]

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, './images/ara.png')
    # dx and dy represent the target position for the player
    self.dx = 93
    self.dy = 93
    self.pos_x = 2
    self.pos_y = 2
    self.reset()
    self.radius = 0.8

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()
  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y

  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]
