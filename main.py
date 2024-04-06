# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# fill the screen with a color to wipe away anything from last frame
# create a surface with the same size as the screen
drawing = pygame.Surface(screen.get_size())
# fill the surface with purple color
drawing.fill("white")
# blit the drawing surface onto the screen

mousedown=False
mousepos=(0,0)
color=0
rgb_color = pygame.Color(0)
addcolor=0
pen_size=50
pen_size_add=0
while running:

    


    
    # RENDER YOUR GAME HERE
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    #mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    screen.blit(drawing, (0, 0))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown=True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown=False
        elif event.type == pygame.MOUSEMOTION:
            mousepos=event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drawing.fill("white")
            elif event.key == pygame.K_UP:
                addcolor=1
            elif event.key == pygame.K_DOWN:
                addcolor=-1
            elif event.key == pygame.K_LEFT:
                pen_size_add=-1
            elif event.key == pygame.K_RIGHT:
                pen_size_add=1
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                # Ctrl+S is pressed
                #file_path = filedialog.asksaveasfilename()
                print("Ctrl+S is pressed")
                # Add your code here to handle the Ctrl+S event
                pen_size_add=1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                addcolor=0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                pen_size_add=0
                
    surface = drawing if mousedown else screen
    # convert HSB to RGB
    pen_size+=pen_size_add
    if pen_size<0:
        pen_size=0
    color = (color+addcolor)%360
    rgb_color.hsva = (color, 100, 100)
    pen_rect = (mousepos[0]-pen_size//2, mousepos[1]-pen_size//2, pen_size, pen_size)
    #print(type(mousepos))
    pygame.draw.ellipse(surface, rgb_color, pen_rect)
    #pygame.draw.ellipse(surface, (color,255,255), (*mousepos, 50, 50))

            #mouse_pos = pygame.mouse.get_pos()
            #pygame.draw.ellipse(screen, "red", (*mouse_pos, 50, 50))
            #pygame.draw.ellipse(screen, "red", (*event.pos,50, 50))
    # flip() the display to put your work on screen
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()