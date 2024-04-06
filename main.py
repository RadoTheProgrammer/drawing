# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# fill the screen with a color to wipe away anything from last frame
screen.fill("purple")
mousedown=False
while running:

    


    
    # RENDER YOUR GAME HERE
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    #mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown=True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown=False
        elif event.type == pygame.MOUSEMOTION:
            if mousedown:
                pygame.draw.ellipse(screen, "red", (*event.pos, 50, 50))
            #mouse_pos = pygame.mouse.get_pos()
            #pygame.draw.ellipse(screen, "red", (*mouse_pos, 50, 50))
            #pygame.draw.ellipse(screen, "red", (*event.pos,50, 50))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()