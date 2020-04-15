import pygame

pygame.init()
done = False

HubWidth = 500
HubHeight = 500
screen = pygame.display.set_mode((HubWidth, HubHeight))
clock = pygame.time.Clock()

Red = 255
Green = 255
Blue = 0

TitleFont = pygame.font.SysFont('Bahnschrift', 100)
RegularFont = pygame.font.SysFont('Century Gothic', 20)
GameFont = pygame.font.SysFont('Candara Bold', 50)

HelpText = RegularFont.render("Pick a game:", False, (255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

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

    if 200 <= MouseY <= 235:
        PongText = GameFont.render("PONG", False, (Red, Green, Blue))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            from Pong import PongGame
            PongGame.run()
    else:
        PongText = GameFont.render("PONG", False, (255, 255, 255))

    if 250 <= MouseY <= 285:
        TicTacToeText = GameFont.render("Work In Progress", False, (255, 100, 100))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            TicTacToeText = GameFont.render("Unavailable", False, (255, 100, 100))
    else:
        TicTacToeText = GameFont.render("Tic Tac Toe (WIP)", False, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(TitleText, (0, 0))
    screen.blit(HelpText, (10, 130))
    screen.blit(PongText, (50, 200))
    screen.blit(TicTacToeText, (50, 250))

    pygame.display.flip()
    clock.tick(60)