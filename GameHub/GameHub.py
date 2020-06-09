import pygame
from Pong import PongGame
from TTT import TicTacToe
from SimonSays import enFil
# Imports PyGame and our games.

pygame.init()
done = False  # This will be useful later :)

HubWidth = 500
HubHeight = 500  # Setting the dimensions for the hub.
clock = pygame.time.Clock()  # I use this to set the FPS to 60 in the bottom.

Red = 255
Green = 255
Blue = 0  # All These are the current values of each RGB color.

TitleFont = pygame.font.SysFont('Bahnschrift', 100)
RegularFont = pygame.font.SysFont('Century Gothic', 30)
GameFont = pygame.font.SysFont('Candara Bold', 50)      # Defining the fonts and font sizes.

HelpText = RegularFont.render("Pick a game:", False, (255, 255, 255))                        # Defining the text that
ByText = RegularFont.render("Made By Krølse, Papa D, TuristGuden.", False, (255, 255, 255))  # won't be changing color

SimonSays = enFil  # Because Emil is good at naming files :)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Ends the program if the game window is closed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True  # Ends the program if escape is pressed.

    screen = pygame.display.set_mode((HubWidth, HubHeight))  # This is the display.

    if Red > 0 and Green == 255 and Blue < 255:
        Red -= 5
        Blue += 5
    if Red < 255 and Green > 0 and Blue == 255:
        Red += 5
        Green -= 5
    if Red == 255 and Green < 255 and Blue > 0:
        Green += 5
        Blue -= 5
    # This created the rainbow effect

    MouseX, MouseY = pygame.mouse.get_pos()  # Getting the cursor's position.

    TitleText = TitleFont.render("Game Hub", False, (Red, Green, Blue))  # This is down here so it can change color.

    if 175 <= MouseY <= 210:
        PongText = GameFont.render("PONG", False, (Red, Green, Blue))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            PongGame.run()
            # These 4 lines allow PONG to be opened by pressing the text that says "PONG"
            # The second of them (line 52) makes the text colorful.
    else:
        PongText = GameFont.render("PONG", False, (255, 255, 255))
        # This is what happens when your cursor is not on the PONG button.

    # The other game titles work the same way as PONG.

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
    screen.blit(ByText, (10, HubHeight - 25))
    # Fills the screen with the color black and writes things on top.

    pygame.display.flip()
    clock.tick(60)
    # This makes the hub go at 60 fps.
