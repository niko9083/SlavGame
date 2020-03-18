import pygame
import random

class BallClass:
    xspeed = 5
    yspeed = 2
    height = 20
    width = 20
    color = (255, 255, 255)

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def update(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, self.width, self.height))