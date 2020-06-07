import pygame, random, sys, time, os
from pygame.locals import *

def run():
    pygame.init()

    #color initialization
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    DARKRED = (128, 0, 0)
    DARKBLUE = (0, 0, 128)
    DARKGREEN = (0, 128, 0)
    DARKYELLOW = (128, 128, 0)

    #sets up the screen
    screen_width = 350
    screen_height = 350
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Simon Says')
    screen.fill(WHITE)
    pygame.display.update()

    #set up for the squares
    button_width = 150
    button_height = 150

    button_red = pygame.Rect(0,0, button_width, button_height)
    button_blue = pygame.Rect(screen_width - button_width, 0, button_width, button_height)
    button_green = pygame.Rect(screen_width - button_width, screen_height - button_height, button_width, button_height)
    button_yellow = pygame.Rect(0, screen_height - button_height, button_width, button_height)

    pygame.draw.rect(screen, RED, button_red)
    pygame.draw.rect(screen, BLUE, button_blue)
    pygame.draw.rect(screen, GREEN, button_green)
    pygame.draw.rect(screen, YELLOW, button_yellow)

    def reset():
        pygame.draw.rect(screen, RED, button_red)
        pygame.draw.rect(screen, BLUE, button_blue)
        pygame.draw.rect(screen, GREEN, button_green)
        pygame.draw.rect(screen, YELLOW, button_yellow)

    GAMEOVER = False
    count = 0;
    clicks = 0;
    clickPositions = []
    rectSequence = []
    randoms = []
    sequence = []
    clickSequence = []
    log = []
    colors = [DARKRED, DARKBLUE, DARKGREEN, DARKYELLOW]
    regColors = ["RED","BLUE","GREEN","YELLOW"]

    buttons = [button_red, button_blue, button_green, button_yellow]

    pygame.display.update()
    HighScore=0

    dirname = os.path.dirname(__file__)
    wiiPath = os.path.join(dirname, 'wii.mp3')
    pygame.mixer.music.load(wiiPath)
    pygame.mixer.music.play(-1)
    score = 0
    while not GAMEOVER:


        r = random.randint(0,3)
        randoms.append(r)
        sequence.append(colors[r])
        rectSequence.append(buttons[r])
        log.append(regColors[r])
        print(log)
        print(rectSequence)
        #print(randoms)

        for index,color in enumerate(sequence):
            time.sleep(.5)
            pygame.draw.rect(screen,color,buttons[randoms[index]])
            pygame.display.update()
            time.sleep(.5)
            reset()
            pygame.display.update()


        count += 1
        print("Count = ", count)

        #the click detection loop
        clicks = -1
        clickPositions = []
        while clicks < count:

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    clicks += 1
                    print("Clicks = ", clicks)
                    clickPositions.append(pygame.mouse.get_pos())
                    print(clickPositions)
                    score = score + 10

        for index,shape in enumerate(rectSequence):
             if not shape.collidepoint(clickPositions[index]):
                print("BAD CLICK")
                try:
                    with open('HighScore.txt') as file:
                        data = file.read()
                        highscore = str(data.strip())
                except:
                    print("highScoreFile not found, resetting to 0.")
                highscore1 = highscore
                file.close()
                font = pygame.font.SysFont('Raleway Bold', 35)

                textScore = font.render("din score er: " + str(score), False, (0, 0, 0))
                textHighScore = font.render("nuværene highscore er " + highscore1, False, (0, 0, 0))
                screen.fill((255, 255, 255))
                screen.blit(textScore, (160 - textScore.get_width() // 2, 100 - textScore.get_height() // 2))
                screen.blit(textHighScore,
                            (170 - textHighScore.get_width() // 2, 200 - textHighScore.get_height() // 2))
                pygame.display.flip()
                time.sleep(10)
                pygame.mixer.music.fadeout(2)
                GAMEOVER = True
                print("score:", score)
                try:
                    with open('HighScore.txt') as file:
                        data = file.read()
                        HighScore = int(data.strip())
                        print("Loaded highscore:", HighScore)
                except:
                    print("highScoreFile not found, resetting to 0.")
                if score > HighScore:
                     try:

                        with open('HighScore.txt','w') as file:
                            file.write(str(score))
                            file.close()
                     except:
                        print("you are shit")
                     print("new highscore",score,"!")
             else:
                print("GOOD CLICK")
