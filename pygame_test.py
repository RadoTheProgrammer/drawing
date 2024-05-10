import os

os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["DISPLAY"] = ":0"

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True

while running:
    print("Hello")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (320, 240), 50)
    pygame.display.flip()

pygame.quit()
