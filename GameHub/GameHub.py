import pygame
from Pong import PongGame
from TTT import TicTacToe
from SimonSays import enFil

pygame.init()
done = False

HubWidth = 500
HubHeight = 500
clock = pygame.time.Clock()

Red = 255
Green = 255
Blue = 0

TitleFont = pygame.font.SysFont('Bahnschrift', 100)
RegularFont = pygame.font.SysFont('Century Gothic', 20)
GameFont = pygame.font.SysFont('Candara Bold', 50)

HelpText = RegularFont.render("Pick a game:", False, (255, 255, 255))
ByText = RegularFont.render("Made By Krølse Papa D, TuristGuden.", False, (255, 255, 255))

SimonSays = enFil

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen = pygame.display.set_mode((HubWidth, HubHeight))

    if Red > 0 and Green == 255 and Blue < 255:
        Red -= 5
        Blue += 5
    if Red < 255 and Green > 0 and Blue == 255:
        Red += 5
        Green -= 5
    if Red == 255 and Green < 255 and Blue > 0:
        Green += 5
        Blue -= 5

    MouseX, MouseY = pygame.mouse.get_pos()

    TitleText = TitleFont.render("Game Hub", False, (Red, Green, Blue))

    if 175 <= MouseY <= 210 and:
        PongText = GameFont.render("PONG", False, (Red, Green, Blue))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            PongGame.run()
    else:
        PongText = GameFont.render("PONG", False, (255, 255, 255))

    if 225 <= MouseY <= 260:
        SimonSaysText = GameFont.render("Simon Says", False, (Red, Green, Blue))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            SimonSays.run()
    else:
        SimonSaysText = GameFont.render("Simon Says", False, (255, 255, 255))

    if 275 <= MouseY <= 310:
        TicTacToeText = GameFont.render("Tic Tac Toe", False, (Red, Green, Blue))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            TicTacToe.run()
    else:
        TicTacToeText = GameFont.render("Tic Tac Toe", False, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(TitleText, (0, 0))
    screen.blit(HelpText, (10, 130))
    screen.blit(PongText, (50, 175))
    screen.blit(SimonSaysText, (50, 225))
    screen.blit(TicTacToeText, (50, 275))
    screen.blit(ByText, (0, HubHeight - 25))

    pygame.display.flip()
    clock.tick(60)