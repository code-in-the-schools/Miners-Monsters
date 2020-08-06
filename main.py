import pygame
import os
 #movement
class Player():
  def __init__(self):
    #load sprite
    pygame.sprite.Sprite.__init__(self)
    Player.image = pygame.image.load("player.png")
    self.image = Player.image
    self.image = pygame.transform.scale(50, 50)
    self.x = 50 
    self.y = 50

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))

p = Player()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  screen.fill((255, 255, 255))
  p.draw(screen)
  pygame.display.update()
