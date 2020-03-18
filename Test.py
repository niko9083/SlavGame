import pygame

done = False

x = 0
y = 0
z = 255

screen = pygame.display.set_mode((400, 400))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    if x < 255 and y == 0 and z == 255:
        x += 1

    if x == 255 and y == 0 and z > 0:
        z -= 1

    screen.fill((x, y, z))