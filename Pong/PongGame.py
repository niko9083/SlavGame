import pygame
from Pong.Player import PlayerClass
from Pong.Ball import BallClass

def run():
    pygame.init()
    done = False

    WindowWidth = 1000
    WindowHeight = 900
    screen = pygame.display.set_mode((WindowWidth, WindowHeight))
    clock = pygame.time.Clock()

    PlayerOne = PlayerClass(100, 400, WindowHeight)
    PlayerTwo = PlayerClass(WindowWidth - 100 - PlayerClass.width, 400, WindowHeight)
    Ball = BallClass(500, 500)

    PP1 = 0
    PP2 = 0
    SpeedCounter = 0

    MyFont = pygame.font.SysFont('Bahnschrift', 100)
    ScoreText = MyFont.render('SCORE', False, (255, 255, 255))

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
            Ball.xpos = 500
            Ball.ypos = PlayerTwo.ypos + PlayerTwo.height / 2
            PP2 += 1
            SpeedCounter += 1
        if Ball.xpos > WindowWidth - Ball.width:
            Ball.xspeed *= -1
            Ball.xpos = 500
            Ball.ypos = PlayerOne.ypos + PlayerOne.height / 2
            PP1 += 1
            SpeedCounter += 1

        # - Players:
        if Ball.ypos + Ball.height >= PlayerOne.ypos and Ball.ypos < PlayerOne.ypos + PlayerOne.height and PlayerOne.xpos + PlayerOne.width >= Ball.xpos >= PlayerOne.xpos:
            Ball.xspeed *= -1
            HitPlayerSound.play()
            if (Ball.yspeed == 2 and PlayerOne.speed < 0) or (Ball.yspeed == -2 and PlayerOne.speed > 0):
                Ball.yspeed *= -1

        if Ball. ypos + Ball.height >= PlayerTwo.ypos and Ball.ypos < PlayerTwo.ypos + PlayerTwo.height and Ball.xpos + Ball.width >= PlayerTwo.xpos and Ball.xpos <= PlayerTwo.xpos + PlayerTwo.width:
            Ball.xspeed *= -1
            if (Ball.yspeed == 2 and PlayerTwo.speed < 0) or (Ball.yspeed == -2 and PlayerTwo.speed > 0):
                Ball.yspeed *= -1

        # Ball.xspeed increases with every 10 total points:
        if SpeedCounter >= 10:
            Ball.xspeed += 2
            SpeedCounter -= SpeedCounter

        CountText = MyFont.render((str(PP1)+"/"+str(PP2)), False, (255, 255, 255))

        PlayerOne.update()
        PlayerTwo.update()
        Ball.update()

        screen.fill((0, 0, 0))
        PlayerOne.draw(screen)  # Left
        PlayerTwo.draw(screen)  # Right
        Ball.draw(screen)
        pygame.draw.rect(screen, (255, 255, 255), (0, 110, WindowWidth, 10))
        screen.blit(ScoreText, (250, 0))
        screen.blit(CountText, (610, 0))

        pygame.display.flip()
        clock.tick(60)