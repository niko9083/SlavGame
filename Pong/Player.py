import pygame

class PlayerClass:
    speed = 0
    maxspeed = 0.3
    height = 150
    width = 20
    color = (255, 255, 255)

    def __init__(self, xpos, ypos, WindowHeight):
        self.xpos = xpos
        self.ypos = ypos
        self.WindowHeight = WindowHeight

    def update(self):
        self.ypos += self.speed
        if self.ypos < 0:
            self.ypos = 0
            self.speed = 0
        if self.ypos > self.WindowHeight - self.height:
            self.ypos = self.WindowHeight - self.height
            self.speed = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, self.width, self.height))