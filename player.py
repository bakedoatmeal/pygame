from gameObject import GameObject

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'ara.png')
    # dx and dy represent the target position for the player
    self.dx = 0
    self.dy = 0
    self.reset()

  def left(self):
    if self.dx >= 100:
      self.dx -= 100

  def right(self):
    if self.dx <= 300:
      self.dx += 100

  def up(self):
    if self.dy >= 100:
      self.dy -= 100

  def down(self):
    if self.dy <= 300:
      self.dy += 100

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32
