from pygame.math import Vector2

#COLOR
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#WINDOW SIZE
WINDOW_WIDTH = 30
WINDOW_HEIGHT = 30
FRAMES_PER_SECOND = 2
PIXEL = 20

#SNAKE STARTER
START_DIRECTION = (0, -PIXEL)
FOODPOS = Vector2(5, 7)
START_SNAKEBODY = [Vector2(15 * PIXEL, 15 * PIXEL),
                   Vector2(15 * PIXEL, 16 * PIXEL),
                   Vector2(15 * PIXEL, 17 * PIXEL)]
