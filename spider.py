import pygame
from constants import *

class Spider:
    COL = [-2, -1, 1, 2, -2, -1, 1, 2]
    ROW = [-1, -2, -2, -1, 1, 2, 2, 1]
    
    def __init__(self, color=RED):
        self.color = color
        self.row = 7
        self.col = 7
        self.x = 0
        self.y = 0
        self.score = 0

    def collectAnt(self, ant, surface):
        ant.reset()
        ant.draw(surface)
        self.increaseScore()
    
    def checkPosition(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def move(self, i):
        self.row += self.ROW[i]
        self.col += self.COL[i]

    def draw(self, surface):
        self.checkPosition()
        pygame.draw.rect(surface, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        
        centre = SQUARE_SIZE//2
        radius = 3
        circleMiddle = (self.x+centre-radius,self.y+8)
        circleMiddle2 = (self.x + SQUARE_SIZE -radius*2, self.y+8)
        pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
        pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
        
    def increaseScore(self):
        self.score += 1

    def reset(self):
        self.row = 7
        self.col = 7
        self.x = 0
        self.y = 0
        self.score = 0
    
    def isOutOfScreen(self, surface):
        return self.row < 0 or self.row > 15 or self.col < 0 or self.col > 15

