import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
STONE_INTERVAL = 30

class Stone:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def update(self):
    if self.y < SCREEN_HEIGHT:
      self.y += 1
    
  def draw(self):
    pyxel.blt(self.x,self.y,0,8,0,8,8, pyxel.COLOR_BLACK)

class App:
  def __init__(self):
    pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title='サプーゲーム')
    pyxel.mouse(True)
    pyxel.load("my_resource.pyxres")
    self.player_x = SCREEN_WIDTH // 2
    self.player_y = SCREEN_HEIGHT * 4 // 5
    self.stones = []
    self.is_collision = False
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_ESCAPE):
      pyxel.quit()

    if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 12:
      self.player_x += 1
    elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -4:
      self.player_x -= 1

    if pyxel.frame_count % STONE_INTERVAL == 0:
      self.stones.append(Stone(pyxel.rndi(0, SCREEN_WIDTH - 8), 0))

    for stone in self.stones.copy():
      stone.update()

      if (self.player_x <= stone.x <= self.player_x + 8 and self.player_y <= stone.y <= self.player_y + 8):
        self.is_collision = True

      if stone.y >= SCREEN_HEIGHT:
        self.stones.remove(stone)

  def draw(self):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    for stone in self.stones:
      stone.draw()
    pyxel.blt(self.player_x, self.player_y, 0,16,0,16,16, pyxel.COLOR_BLACK)
    
    if self.is_collision:
      pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "Game Over", pyxel.COLOR_YELLOW)
    

App()