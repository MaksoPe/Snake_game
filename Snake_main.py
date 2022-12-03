# pygame demo 4(b) - one image, bounce around the window using rects
# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from Snake import *
from Snake_game_start_constants import *

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH * PIXEL, WINDOW_HEIGHT * PIXEL))
clock = pygame.time.Clock()

#5 - Initailze variables
oSnake = Snake(window)


#6 - Loop forever
while True:
    #7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                oSnake.moveUp()
            if event.key == K_DOWN:
                oSnake.moveDown()
            if event.key == K_RIGHT:
                oSnake.moveRight()
            if event.key == K_LEFT:
                oSnake.moveLeft()
             
    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    oSnake.moveSnake()
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
        
