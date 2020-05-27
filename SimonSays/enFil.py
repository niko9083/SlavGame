import pygame, random, sys, time
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

    pygame.mixer.music.load('music/wii.mp3')
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
        clicks = 0
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
    font = pygame.font.SysFont("comicsansms", 40)

    text = font.render("your score is: " + str(score), False, (0, 128, 0))

    while GAMEOVER:
        screen.fill((255, 255, 255))
        screen.blit(text,
                    (120 - text.get_width() // 2, 100 - text.get_height() // 2))

        pygame.display.flip()