#Snake class

import pygame
import random
from pygame.math import Vector2
from Snake_game_start_constants import *


class Snake():
    def __init__(self, window):
        self.window = window
        self.width = WINDOW_WIDTH #30 rows, 600x600 with pixels
        self.height = WINDOW_HEIGHT #30 columns, 600x600 with pixels
        self.pixel = PIXEL

        self.snakeColor = GREEN
        self.eggColor = WHITE

        #StartPositions:
        self.direction = START_DIRECTION
        self.foodPos = FOODPOS
        self.SnakeBody = START_SNAKEBODY
                                  
    def gameStart(self):
        self.direction = START_DIRECTION
        self.foodPos = FOODPOS
        self.SnakeBody = START_SNAKEBODY
        
    def collisionTest(self):
        #Snake collision with window frame
        if (self.SnakeBody[0].x < 0 or
            (self.SnakeBody[0].x + self.pixel) > (self.width * self.pixel) or
            self.SnakeBody[0].y < 0 or
            (self.SnakeBody[0].y + self.pixel)> (self.height * self.pixel)):
            self.gameStart()
        #Snake collision with body
        if self.SnakeBody[0] in self.SnakeBody[1:]:
            self.gameStart()       

    def draw(self):
        #Drawing all snake rectangles
        for vector in self.SnakeBody:
            bodyRect = pygame.Rect(vector.x, vector.y, self.pixel, self.pixel)
            pygame.draw.rect(self.window, self.snakeColor, bodyRect)
            
        #Draw one food rect  
        self.eggRect = pygame.Rect(self.foodPos.x * self.pixel,
                                   self.foodPos.y * self.pixel,
                                   self.pixel,
                                   self.pixel)
        pygame.draw.rect(self.window, self.eggColor, self.eggRect)
                                                            
    def moveSnake(self):
        #Is there a game ending collison? (wall/SnakeBody)
        self.collisionTest()
        
        #Snake head moved to a position which is the food
        if self.SnakeBody[0] == self.foodPos * self.pixel:
            SnakeBodyCopy = self.SnakeBody[:]
            SnakeBodyCopy.insert(0, SnakeBodyCopy[0] + self.direction)
            self.SnakeBody = SnakeBodyCopy
            #Create another food pos:
            self.foodPos.x = random.randint(0, self.width -1)
            self.foodPos.y = random.randint(0, self.height -1)
        #Snake head moved to a position which is NOT the food
        else:
            SnakeBodyCopy = self.SnakeBody[:-1]
            SnakeBodyCopy.insert(0, SnakeBodyCopy[0] + self.direction)
            self.SnakeBody = SnakeBodyCopy
        #Draw out the new objects
        self.draw()
                   
    #if clause -> ensures that the snake cannot do a 180 instant turn      
    def moveUp(self):
        if self.direction != (0, self.pixel):
            self.direction = (0, -self.pixel)
            
    def moveDown(self):
        if self.direction != (0, -self.pixel):
            self.direction = (0, self.pixel)
            
    def moveRight(self):
        if self.direction != (-self.pixel, 0):
            self.direction = (self.pixel, 0)
            
    def moveLeft(self):
        if self.direction != (self.pixel, 0):
            self.direction = (-self.pixel, 0)
