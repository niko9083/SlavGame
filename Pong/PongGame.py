#######    #######    ##    #    #######
#     #    #     #    # #   #    #
#######    #     #    #  #  #    #  ####
#          #     #    #   # #    #     #
#          #######    #    ##    #######
import pygame
from Player import PlayerClass
from Pong.Ball import BallClass

pygame.init()
done = False

WindowWidth = 1000
WindowHeight = 900
screen = pygame.display.set_mode((WindowWidth, WindowHeight))
clock = pygame.time.Clock()

PlayerOne = PlayerClass(100, 400, WindowHeight)
PlayerTwo = PlayerClass(WindowWidth - 100 - PlayerClass.width, 400, WindowHeight)
Ball = BallClass(300, 400)

PP1 = 0
PP2 = 0

MyFont = pygame.font.SysFont('Agency FB', 100)
ScoreText = MyFont.render('SCORE', False, (255, 255, 255))
ScoreBar = pygame.draw.rect(screen, (255, 255, 255), (WindowHeight - 100, 0, WindowWidth, 10))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    # Movement and motion:
    # - Press
    if event.type == pygame.KEYDOWN:
        # Player one:
        if event.key == pygame.K_w:
            PlayerOne.speed -= PlayerOne.maxspeed
        if event.key == pygame.K_s:
            PlayerOne.speed += PlayerOne.maxspeed
        # Player two:
        if event.key == pygame.K_UP:
            PlayerTwo.speed -= PlayerTwo.maxspeed
        if event.key == pygame.K_DOWN:
            PlayerTwo.speed += PlayerTwo.maxspeed

    # - Release:
    if event.type == pygame.KEYUP:
        # Player one:
        if event.key == pygame.K_w or event.key == pygame.K_s:
            PlayerOne.speed -= PlayerOne.speed
        # Player two:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            PlayerTwo.speed -= PlayerTwo.speed

    # Ball bounce:
    # - Walls:
    if Ball.ypos < 120 or Ball.ypos > WindowHeight - Ball.height:
        Ball.yspeed *= -1
    if Ball.xpos < 1:
        Ball.xspeed *= -1
        PP2 += 1
        print("Score:",PP1,"/",PP2)
    if Ball.xpos > WindowWidth - Ball.width:
        Ball.xspeed *= -1
        PP1 += 1
        print("Score:",PP1,"/",PP2)
    # - Players:
    if Ball.ypos + Ball.height >= PlayerOne.ypos and Ball.ypos < PlayerOne.ypos + PlayerOne.height and Ball.xpos == PlayerOne.xpos + PlayerOne.width or Ball.ypos + Ball.height >= PlayerTwo.ypos and Ball.ypos < PlayerTwo.ypos + PlayerTwo.height and Ball.xpos + Ball.width == PlayerTwo.xpos:
        Ball.xspeed *= -1

    CountText = MyFont.render((str(PP1) + "/" + str(PP2)), False, (255, 255, 255))

    PlayerOne.update()
    PlayerTwo.update()
    Ball.update()

    screen.fill((0, 0, 0))
    PlayerOne.draw(screen)
    PlayerTwo.draw(screen)
    Ball.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), (0, 110, WindowWidth, 10))
    screen.blit(ScoreText, (320, 0))
    screen.blit(CountText, (550, 0))

    pygame.display.flip()
    clock.tick(60)