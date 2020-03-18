import pygame
from Player import PlayerClass
from PlayerTwo import P2Class
from Ball import BallClass

pygame.init()
done = False

WindowWidth = 1000
WindowHeight = 800

screen = pygame.display.set_mode((WindowWidth, WindowHeight))
clock = pygame.time.Clock()
p1 = PlayerClass(100, 400)
p2 = P2Class(900, 400)
ball = BallClass(WindowWidth / 2, WindowHeight / 2)

    #######    #######    ##    #    ########
    #     #    #     #    # #   #    #
    #######    #     #    #  #  #    #   ####
    #          #     #    #   # #    #      #
    #          #######    #    ##    ########

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    #Movement
    if event.type == pygame.KEYDOWN:
        #Player one movement
        if event.key == pygame.K_w and not p1.ypos <= 0:
            p1.ypos -= p1.maxspeed
        if event.key == pygame.K_s and not p1.ypos >= WindowHeight - p1.height:
            p1.ypos += p1.maxspeed
        #Player two movement
        if event.key == pygame.K_UP and not p2.ypos <= 0:
            p2.ypos -= p2.maxspeed
        if event.key == pygame.K_DOWN and not p2.ypos >= WindowHeight - p2.height:
            p2.ypos += p2.maxspeed
        #Ball bounce
        if ball.xpos <= 0 or ball.xpos >= WindowWidth - ball.width:
            ball.xspeed *= -1
        if ball.ypos <= 0 or ball.ypos >= WindowHeight - ball.height:


    screen.fill((0,0,0))
    p1.draw(screen)
    p2.draw(screen)
    ball.draw(screen)

    pygame.display.flip()